import plotly.express as px
import pandas as pd

def create_plot(
    df: pd.DataFrame,
    x,
    y=None,
    plot_type="Scatter",
    color=None,
    facet_col=None,
    template="plotly",
    marker_size=10,
    opacity=0.8,
    point_color="#636efa"
):
    """
    Create a Plotly figure with optional customization.

    Parameters:
    - df: pd.DataFrame
    - x: column name for x-axis
    - y: column name for y-axis (not required for histogram)
    - plot_type: "Scatter", "Bar", "Histogram", "Box"
    - color: column for grouping colors
    - facet_col: column for faceting
    - template: Plotly theme
    - marker_size: size of points (Scatter only)
    - opacity: marker/bar opacity
    - point_color: single color for scatter if no grouping

    Returns:
    - fig: Plotly figure
    """
    if plot_type == "Scatter":
        fig = px.scatter(
            df,
            x=x,
            y=y,
            color=color if color else None,
            facet_col=facet_col,
            template=template
        )
        # Apply single color if no grouping
        if not color:
            fig.update_traces(marker=dict(size=marker_size, color=point_color), opacity=opacity)
        else:
            fig.update_traces(marker=dict(size=marker_size), opacity=opacity)

    elif plot_type == "Bar":
        fig = px.bar(
            df,
            x=x,
            y=y,
            color=color,
            facet_col=facet_col,
            template=template
        )
        fig.update_traces(opacity=opacity)

    elif plot_type == "Histogram":
        fig = px.histogram(
            df,
            x=x,
            color=color,
            facet_col=facet_col,
            template=template
        )
        fig.update_traces(opacity=opacity)

    elif plot_type == "Box":
        fig = px.box(
            df,
            x=x,
            y=y,
            color=color,
            facet_col=facet_col,
            template=template
        )
        fig.update_traces(opacity=opacity)

    else:
        raise ValueError(f"Unsupported plot type: {plot_type}")

    return fig


def apply_layout(
    fig,
    title=None,
    x_label=None,
    y_label=None,
    font_size=14
):
    """Apply consistent layout and font settings to a Plotly figure."""
    fig.update_layout(
        title=dict(text=title, font=dict(size=font_size)) if title else None,
        xaxis_title=dict(text=x_label, font=dict(size=font_size)) if x_label else None,
        yaxis_title=dict(text=y_label, font=dict(size=font_size)) if y_label else None,
        xaxis=dict(tickfont=dict(size=font_size)),
        yaxis=dict(tickfont=dict(size=font_size)),
        legend=dict(font=dict(size=font_size)),
        font=dict(size=font_size)
    )
    return fig

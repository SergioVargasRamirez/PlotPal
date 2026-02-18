import streamlit as st
import numpy as np
from utils.plot_customization import plot_customization
from utils.plot_utils import create_plot, apply_layout

st.header("📊 Scatter Plot")

# -----------------------------
# Check if dataset exists
# -----------------------------
if "df" not in st.session_state or st.session_state.df.empty:
    st.warning("Please create a dataset first in the Data Entry page.")
    st.stop()

df = st.session_state.df
columns = df.columns.tolist()

# -----------------------------
# Plot Configuration
# -----------------------------
st.subheader("Plot Configuration")

x_col = st.selectbox("X-axis", columns)
y_col = st.selectbox("Y-axis", columns)
color_col = st.selectbox("Grouping / Color (optional)", [None] + columns)
facet_col = st.selectbox("Facet by column (optional)", [None] + columns)

# -----------------------------
# Get customization options
# -----------------------------
custom = plot_customization(
    default_marker_size=10,
    default_opacity=0.8,
    default_font_size=14
)

# -----------------------------
# Prepare data for plotting
# -----------------------------
plot_df = df.copy()

# Apply log10 transformation if selected
if custom["log_x"]:
    plot_df = plot_df[plot_df[x_col] > 0]
    plot_df[x_col] = np.log10(plot_df[x_col])

if custom["log_y"]:
    plot_df = plot_df[plot_df[y_col] > 0]
    plot_df[y_col] = np.log10(plot_df[y_col])

# Update axis labels to indicate log
x_label = custom["x_label"] + (" (log10)" if custom["log_x"] else "")
y_label = custom["y_label"] + (" (log10)" if custom["log_y"] else "")

# -----------------------------
# Generate Scatter Plot
# -----------------------------
try:
    fig = create_plot(
        df=plot_df,
        x=x_col,
        y=y_col,
        plot_type="Scatter",
        color=color_col,
        facet_col=facet_col,
        template=custom["theme"],
        marker_size=custom["marker_size"],
        opacity=custom["opacity"],
        point_color=custom["point_color"]
    )

    fig = apply_layout(
        fig,
        title=custom["title"],
        x_label=x_label,
        y_label=y_label,
        font_size=custom["font_size"]
    )

    st.plotly_chart(fig, width="stretch")

except Exception as e:
    st.error(f"Error generating plot: {e}")

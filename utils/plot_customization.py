import streamlit as st

def plot_customization(default_marker_size=10, default_opacity=0.8, default_font_size=14, default_color="#636efa"):
    """
    Returns user-selected customization options as a dictionary
    """
    st.subheader("Customization")

    marker_size = st.slider("Marker size", 4, 40, default_marker_size)
    opacity = st.slider("Opacity", 0.1, 1.0, default_opacity)
    font_size = st.slider("Font size", 8, 32, default_font_size)
    theme = st.selectbox("Theme", ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn"])
    point_color = st.color_picker("Pick a color (ignored if grouping selected)", default_color)

    title = st.text_input("Plot Title", "My Plot")
    x_label = st.text_input("X-axis Label", "X-axis")
    y_label = st.text_input("Y-axis Label", "Y-axis")

    col1, col2 = st.columns(2)
    with col1:
        log_x = st.checkbox("Log10 X-axis", value=False)
    with col2:
        log_y = st.checkbox("Log10 Y-axis", value=False)

    return {
        "marker_size": marker_size,
        "opacity": opacity,
        "font_size": font_size,
        "theme": theme,
        "point_color": point_color,
        "title": title,
        "x_label": x_label,
        "y_label": y_label,
        "log_x": log_x,
        "log_y": log_y
    }

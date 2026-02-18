import streamlit as st
import pandas as pd

st.header("📥 Data Entry")

# ----------------------
# Initialize session state
# ----------------------
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

if "num_cols" not in st.session_state:
    st.session_state.num_cols = 3

if "num_rows" not in st.session_state:
    st.session_state.num_rows = 5

if "col_names" not in st.session_state:
    st.session_state.col_names = [f"Col{i+1}" for i in range(st.session_state.num_cols)]

if "col_types" not in st.session_state:
    # Default all columns to Text
    st.session_state.col_types = ["Text" for _ in range(st.session_state.num_cols)]

# ----------------------
# Step 1: Configure table (always visible)
# ----------------------
st.subheader("Step 1: Configure Table")

# Number of columns and rows
st.session_state.num_cols = st.number_input(
    "Number of columns:",
    min_value=1,
    max_value=10,
    value=st.session_state.num_cols,
    step=1
)

st.session_state.num_rows = st.number_input(
    "Initial number of rows:",
    min_value=1,
    max_value=20,
    value=st.session_state.num_rows,
    step=1
)

# Adjust col_names and col_types list lengths
if len(st.session_state.col_names) < st.session_state.num_cols:
    st.session_state.col_names += [f"Col{i+1}" for i in range(len(st.session_state.col_names), st.session_state.num_cols)]
    st.session_state.col_types += ["Text"] * (st.session_state.num_cols - len(st.session_state.col_types))
elif len(st.session_state.col_names) > st.session_state.num_cols:
    st.session_state.col_names = st.session_state.col_names[:st.session_state.num_cols]
    st.session_state.col_types = st.session_state.col_types[:st.session_state.num_cols]

# Column name inputs and type selection
for i in range(st.session_state.num_cols):
    col1, col2 = st.columns([2, 1])  # two columns: name and type
    with col1:
        st.session_state.col_names[i] = st.text_input(
            f"Column {i+1} name:",
            value=st.session_state.col_names[i],
            key=f"colname_input_{i}"
        )
    with col2:
        st.session_state.col_types[i] = st.selectbox(
            f"Type {i+1}:",
            ["Text", "Numeric"],
            index=0 if st.session_state.col_types[i] == "Text" else 1,
            key=f"coltype_input_{i}"
        )

# Generate table
if st.button("Generate Table"):
    # Create empty table with appropriate types
    data_dict = {}
    for name, ctype in zip(st.session_state.col_names, st.session_state.col_types):
        if ctype == "Text":
            data_dict[name] = [""] * st.session_state.num_rows
        else:
            data_dict[name] = [0.0] * st.session_state.num_rows
    st.session_state.df = pd.DataFrame(data_dict)
    st.success("Table generated! You can now edit the values below.")

# ----------------------
# Step 2: Editable table
# ----------------------
if not st.session_state.df.empty:
    st.subheader("Step 2: Enter Data")

    edited_df = st.data_editor(
        st.session_state.df,
        num_rows="dynamic",
        width='stretch'
    )

    # Cast columns based on type selection
    for name, ctype in zip(st.session_state.col_names, st.session_state.col_types):
        if ctype == "Text":
            edited_df[name] = edited_df[name].astype(str)
        else:
            edited_df[name] = pd.to_numeric(edited_df[name], errors='coerce')

    if st.button("Load Data"):
        st.session_state.df = edited_df
        st.success("Data Loaded!")

    st.subheader("Current Data Preview")
    st.dataframe(st.session_state.df)

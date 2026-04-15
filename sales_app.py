import streamlit as st
import pandas as pd

# Title and description
st.title("Sales Summary App")
st.subheader("Filter sales data by category")

# Create dataset
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Watch"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Accessories"],
    "Sales": [50000, 2000, 30000, 4000, 7000]
}

df = pd.DataFrame(data)

# Sidebar filter
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data
filtered_df = df[df["Category"] == category]

# Show table
st.dataframe(filtered_df)

# Show chart
st.line_chart(filtered_df["Sales"])
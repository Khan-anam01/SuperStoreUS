import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df  = pd.read_csv("SuperStoreUS.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Order Priority'] = df['Order Priority'].str.strip()

# Sidebar filters
regions = df['Region'].unique()
selected_region = st.sidebar.selectbox("Select Region", options=regions)

# Filtered Data
filtered_df = df[df['Region'] == selected_region]

# KPI Metrics
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
avg_profit_margin = (filtered_df['Profit'] / filtered_df['Sales']).mean()

st.title("Sales Dashboard")
st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Profit", f"${total_profit:,.2f}")
st.metric("Avg Profit Margin", f"{avg_profit_margin:.2%}")

# Sales by Category
category_sales = filtered_df.groupby('Product Category')['Sales'].sum()
st.subheader("Sales by Product Category")
st.bar_chart(category_sales)

# Monthly Sales Trend
monthly_sales = filtered_df.groupby(df['Order Date'].dt.to_period("M"))['Sales'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()
st.subheader("Monthly Sales Trend")
st.line_chart(monthly_sales)

# Sales by Order Priority
priority_sales = filtered_df.groupby('Order Priority')['Sales'].sum()
st.subheader("Sales by Order Priority")
st.bar_chart(priority_sales)

# Sales Dashboard

A comprehensive Streamlit-based sales analytics dashboard for visualizing and analyzing SuperStore sales data across different regions, categories, and time periods.

## Features

- **Interactive Region Filtering**: Select and analyze data for specific regions
- **Key Performance Indicators (KPIs)**: Track total sales, profit, and profit margins
- **Sales Analytics**: 
  - Sales breakdown by product category
  - Monthly sales trends over time
  - Sales analysis by order priority
- **Real-time Updates**: Dashboard updates automatically based on selected filters

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.7 or higher
- Required Python packages (see Installation section)

## Installation

1. **Clone or download the project files**
   ```bash
   git clone https://github.com/Khan-anam01/SuperStoreUS.git
   cd <project-directory>
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pandas matplotlib
   ```

   Or using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify data file location**
   - Ensure the SuperStore dataset is located at: `SuperStoreUS.csv`
   - The path is relative to the script location

## Data Requirements

The application expects a CSV file with the following columns:
- `Order Date`: Date of the order (will be converted to datetime)
- `Region`: Geographic region for filtering
- `Sales`: Sales amount for calculations
- `Profit`: Profit amount for calculations
- `Product Category`: Category classification for grouping
- `Order Priority`: Priority level of orders

## Usage

1. **Start the application**
   ```bash
   streamlit run sales_dashboard.py
   ```

2. **Access the dashboard**
   - Open your web browser and navigate to `http://localhost:8501`
   - The dashboard will load automatically

3. **Using the dashboard**
   - Use the sidebar to select different regions
   - View KPI metrics at the top of the page
   - Analyze various charts and visualizations
   - All charts update automatically when filters change

## Dashboard Components

### KPI Metrics
- **Total Sales**: Sum of all sales in the selected region
- **Total Profit**: Sum of all profits in the selected region  
- **Average Profit Margin**: Average profit margin percentage

### Visualizations
- **Sales by Product Category**: Bar chart showing sales distribution across categories
- **Monthly Sales Trend**: Line chart displaying sales trends over time
- **Sales by Order Priority**: Bar chart analyzing sales by priority levels

## File Structure

```
project-directory/
│
├── sales_dashboard.py          # Main application file
├── requirements.txt            # Python dependencies
├── README.md                  # This file
│
└── SuperStoreUS.csv       # Data file
```

## Customization

### Adding New Filters
To add additional filters, modify the sidebar section:
```python
# Add new filter
categories = df['Product Category'].unique()
selected_category = st.sidebar.selectbox("Select Category", options=categories)

# Update filtered data
filtered_df = df[
    (df['Region'] == selected_region) & 
    (df['Product Category'] == selected_category)
]
```

### Adding New Visualizations
Add new charts after the existing visualizations:
```python
# Example: Sales by Customer Segment
segment_sales = filtered_df.groupby('Customer Segment')['Sales'].sum()
st.subheader("Sales by Customer Segment")
st.bar_chart(segment_sales)
```

### Modifying KPIs
Add or modify KPI calculations:
```python
# Example: Add average order value
avg_order_value = filtered_df['Sales'].mean()
st.metric("Average Order Value", f"${avg_order_value:,.2f}")
```

## Troubleshooting

### Common Issues

1. **File not found error**
   - Verify the CSV file path is correct
   - Check that `SuperStoreUS.csv` exists in the specified location

2. **Module import errors**
   - Ensure all required packages are installed
   - Try reinstalling packages: `pip install --upgrade streamlit pandas matplotlib`

3. **Date parsing issues**
   - Verify that the 'Order Date' column contains valid date formats
   - Check for missing or malformed date values

4. **Empty charts**
   - Ensure the filtered data contains records
   - Check that column names match exactly (case-sensitive)

### Performance Optimization

For large datasets:
- Consider adding data caching: `@st.cache_data`
- Implement data sampling for faster loading
- Use date range filters to limit data processing

## Dependencies

- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **matplotlib**: Plotting library (used by Streamlit charts)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For issues or questions:
- Check the troubleshooting section
- Review Streamlit documentation: https://docs.streamlit.io
- Open an issue in the project repository

---

**Note**: This dashboard is designed for the SuperStore dataset format. Modify column names and data processing logic as needed for different datasets.
import streamlit as st
import plotly.express as px
import pandas as pd

# Attempt to read in the data
try:
    data = pd.read_csv("precious_metals_prices_2018_2021.csv")
    data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d %H:%M:%S")
except Exception as e:
    st.error(f"An error occurred while reading the data: {e}")
    st.stop()

# Initial Plot
initial_fig = px.line(
    data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=data.columns[1:],  # Plotting all metals initially
    color_discrete_map={
        "Platinum": "#E5E4E2",
        "Gold": "gold",
        "Silver": "silver",
        "Palladium": "#CED0DD",
        "Rhodium": "#E2E7E1",
        "Iridium": "#3D3C3A",
        "Ruthenium": "#C9CBC8"
    }
)

st.title("Precious Metal Prices 2018-2021")
st.write("The cost of precious metals between 2018 and 2021")
st.plotly_chart(initial_fig, use_container_width=True)

# User Input for Metal Filter
selected_metal = st.selectbox("Select Metal", data.columns[1:], index=0)

# User Input for Date Range Filter
start_date = st.date_input("Start Date", min_value=data["DateTime"].min().date(), max_value=data["DateTime"].max().date(), value=data["DateTime"].min().date())
end_date = st.date_input("End Date", min_value=data["DateTime"].min().date(), max_value=data["DateTime"].max().date(), value=data["DateTime"].max().date())

# Filtering Data Based on User Input
filtered_data = data.loc[(data.DateTime >= pd.Timestamp(start_date)) & (data.DateTime <= pd.Timestamp(end_date))]

# Updated Plotly Chart
fig = px.line(
    filtered_data,
    title=f"{selected_metal} Prices from {start_date} to {end_date}",
    x="DateTime",
    y=selected_metal,
    color_discrete_map={selected_metal: "gold"}  # Update this based on your preference
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Price (USD/oz)",
    font=dict(
        family="Verdana, sans-serif",
        size=18,
        color="white"
    ),
)

# Display Updated Plotly Chart
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d %H:%M:%S")

# Create a plotly plot for use by st.plotly_chart().
fig = px.line(
    data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=["Gold"],
    color_discrete_map={"Gold": "gold"}
)

st.title("Precious Metal Prices 2018-2021")

# Header Description
st.write("The cost of precious metals between 2018 and 2021")

# Metal Filter
selected_metal = st.selectbox("Select Metal", data.columns[1:], index=0)

# Date Range Filter
start_date = st.date_input("Start Date", min_value=data["DateTime"].min().date(), max_value=data["DateTime"].max().date(), value=data["DateTime"].min().date())
end_date = st.date_input("End Date", min_value=data["DateTime"].min().date(), max_value=data["DateTime"].max().date(), value=data["DateTime"].max().date())

filtered_data = data.loc[(data.DateTime >= str(start_date)) & (data.DateTime <= str(end_date))]

# Plotly Chart
fig = px.line(
    filtered_data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=[selected_metal],
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

# Display Plotly Chart
st.plotly_chart(fig, use_container_width=True)

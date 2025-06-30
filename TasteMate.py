import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📊 TasteMate Repeat Order Dashboard")
st.markdown("This dashboard provides deep insights into customer behavior, repeat orders, pricing trends, and more using the TasteMate dataset.")

# Load data
df = pd.read_csv("TasteMate.csv")

# Rename and clean
df.rename(columns={'Repaet labels ': 'Repeat_Label'}, inplace=True)

# Sidebar Filters
st.sidebar.header("🔍 Filters")
selected_city = st.sidebar.multiselect("Select City", options=df['City'].unique(), default=df['City'].unique())
selected_gender = st.sidebar.multiselect("Select Gender", options=df['sex'].unique(), default=df['sex'].unique())
price_range = st.sidebar.slider("Select Price Range", float(df['price'].min()), float(df['price'].max()), (20.0, 80.0))

filtered_df = df[
    (df['City'].isin(selected_city)) &
    (df['sex'].isin(selected_gender)) &
    (df['price'] >= price_range[0]) & 
    (df['price'] <= price_range[1])
]

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Customer Insights", "Order Behavior", "Repeat Order Analysis", "City & Restaurant Trends"])

with tab1:
    st.header("👥 Customer Insights")
    st.write("Analyze customer distribution by demographics and preferences.")

    st.subheader("Gender Distribution")
    st.plotly_chart(px.pie(filtered_df, names='sex', title='Gender Distribution'))

    st.subheader("Income Percentage Distribution")
    st.plotly_chart(px.histogram(filtered_df, x='income_persentage', nbins=20, color='sex'))

    st.subheader("Meal Preference by Gender")
    st.plotly_chart(px.histogram(filtered_df, x='Meal_Preference', color='sex', barmode='group'))

with tab2:
    st.header("🍽️ Order Behavior")
    st.write("Understand patterns in pricing, meal types, and ordering frequency.")

    st.subheader("Price Distribution")
    st.plotly_chart(px.box(filtered_df, x='sex', y='price', color='sex', title='Price by Gender'))

    st.subheader("Hot vs Cold Meals")
    st.plotly_chart(px.histogram(filtered_df, x='hot_cold', color='sex', barmode='group'))

    st.subheader("Days Since Last Order Distribution")
    st.plotly_chart(px.histogram(filtered_df, x='Days_Since_Last_Order', nbins=20, color='sex'))

with tab3:
    st.header("🔁 Repeat Order Analysis")
    st.write("Discover factors contributing to repeat orders.")

    st.subheader("Repeat vs Non-Repeat Customer Count")
    st.plotly_chart(px.histogram(filtered_df, x='Repeat_Label', color='sex'))

    st.subheader("Price vs Repeat Order")
    st.plotly_chart(px.box(filtered_df, x='Repeat_Label', y='price', color='Repeat_Label'))

    st.subheader("Meal Type and Repeat Order")
    st.plotly_chart(px.histogram(filtered_df, x='Meal_Preference', color='Repeat_Label', barmode='group'))

with tab4:
    st.header("🌆 City & Restaurant Trends")
    st.write("View geographic and restaurant-type insights.")

    st.subheader("City-Wise Customer Distribution")
    st.plotly_chart(px.pie(filtered_df, names='City', title='Customers by City'))

    st.subheader("Restaurant Type Preferences")
    st.plotly_chart(px.histogram(filtered_df, x='Restaurant_Type', color='sex'))

    st.subheader("Serve Type vs Repeat Order")
    st.plotly_chart(px.histogram(filtered_df, x='Serve_Type', color='Repeat_Label', barmode='group'))

# Footer
st.markdown("---")
st.markdown("✅ Dashboard powered by Streamlit | Built for HR & Stakeholders | All visuals dynamically update with filters")

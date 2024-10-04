import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

merged_df = pd.read_csv('main_data.csv')

top_10_product_category = merged_df.groupby('product_category_name_english')['order_id'].count().sort_values(ascending=False).head(10)

top_10_product_category_df = top_10_product_category.reset_index()
top_10_product_category_df.columns = ['Kategori Produk', 'Angka Penjualan']

st.title('Kategori Produk yang Paling Laris')

st.dataframe(top_10_product_category_df)

st.title('Diagram data angka penjualan')
st.write('pada diagram ini, terdapat kategori-kategori produk yang paling laris')

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_10_product_category_df['Kategori Produk'], y=top_10_product_category_df['Angka Penjualan'], ax=ax)

ax.set_title('Kategori Produk yang paling laris')
ax.set_xlabel('Kategori Produk')
ax.set_ylabel('Angka Penjualan')
ax.set_xticklabels(top_10_product_category_df['Kategori Produk'], rotation=45, ha='right')

for i, value in enumerate(top_10_product_category_df['Angka Penjualan']):
    ax.text(i, value + 0.5, f'{value}', ha='center')

st.pyplot(fig)

merged_df['order_delivered_customer_date'] = pd.to_datetime(merged_df['order_delivered_customer_date'], errors='coerce')
merged_df['order_purchase_timestamp'] = pd.to_datetime(merged_df['order_purchase_timestamp'], errors='coerce')
merged_df['order_estimated_delivery_date'] = pd.to_datetime(merged_df['order_estimated_delivery_date'], errors='coerce')

merged_df['actual_delivery_time'] = (merged_df['order_delivered_customer_date'] - merged_df['order_purchase_timestamp']).dt.days
merged_df['estimated_delivery_time'] = (merged_df['order_estimated_delivery_date'] - merged_df['order_purchase_timestamp']).dt.days

merged_df['purchase_month'] = merged_df['order_purchase_timestamp'].dt.to_period('M')

delivery_trend = merged_df.groupby('purchase_month')[['actual_delivery_time', 'estimated_delivery_time']].mean().dropna()

st.title('Trend waktu perkiraan dan waktu nyata')

st.line_chart(delivery_trend)

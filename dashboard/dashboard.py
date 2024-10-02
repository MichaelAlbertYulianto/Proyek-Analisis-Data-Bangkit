import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

payment_df = pd.read_csv("D:\Bangkit\Analisis Data  E-Commerce Public\Proyek-Analisis-Data-Bangkit\data\olist_order_payments_dataset.csv")
category_df = pd.read_csv("D:\Bangkit\Analisis Data  E-Commerce Public\Proyek-Analisis-Data-Bangkit\data\product_category_name_translation.csv")
product_df = pd.read_csv("D:\Bangkit\Analisis Data  E-Commerce Public\Proyek-Analisis-Data-Bangkit\data\olist_products_dataset.csv")
order_item_df = pd.read_csv("D:\Bangkit\Analisis Data  E-Commerce Public\Proyek-Analisis-Data-Bangkit\data\olist_order_items_dataset.csv")
customers_df = pd.read_csv("D:\Bangkit\Analisis Data  E-Commerce Public\Proyek-Analisis-Data-Bangkit\data\olist_customers_dataset.csv")
order_df = pd.read_csv("D:\Bangkit\Analisis Data  E-Commerce Public\Proyek-Analisis-Data-Bangkit\data\olist_orders_dataset.csv")

merged_df = pd.merge(order_item_df, product_df, on='product_id', how='left')

merged_df = pd.merge(merged_df, category_df, on='product_category_name', how='left')

merged_df = pd.merge(merged_df, payment_df, on='order_id', how='left')

merged_df = pd.merge(merged_df, order_df, on='order_id', how='left')

merged_df = pd.merge(merged_df, customers_df, on='customer_id', how='left')

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

top_10_customer_city = merged_df.groupby('customer_city')['order_id'].count().sort_values(ascending=False).head(10)

top_10_customer_city_df = top_10_customer_city.reset_index()
top_10_customer_city_df.columns = ['Customer City', 'Number of Orders']

st.title('Kota dengan Pelanggan Terbanyak')

st.dataframe(top_10_customer_city_df)

st.title('Diagram data jumlah pesanan')
st.write('Pada diagram ini, terdapat kota-kota dengan pelanggan terbanyak berdasarkan jumlah pesanan.')

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_10_customer_city_df['Customer City'], y=top_10_customer_city_df['Number of Orders'], ax=ax)

ax.set_title('Kota dengan pelanggan terbanyak')
ax.set_xlabel('Kota Pelanggan')
ax.set_ylabel('Jumlah Pesanan')
ax.set_xticklabels(top_10_customer_city_df['Customer City'], rotation=45, ha='right')

for i, value in enumerate(top_10_customer_city_df['Number of Orders']):
    ax.text(i, value + 0.5, f'{value}', ha='center')

st.pyplot(fig)

merged_df.to_csv('main_data.csv', index=False)
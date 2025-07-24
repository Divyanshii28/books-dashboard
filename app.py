import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Set Streamlit page config at the very top!
st.set_page_config(page_title="Books Dashboard", layout="wide")

# Load JSON data
@st.cache_data
def load_data():
    with open("Books.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)

df = load_data()
st.title("📚 Books Data Analysis Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Books")
categories = st.sidebar.multiselect("Select Categories", sorted(df['category'].unique()), default=sorted(df['category'].unique()))
min_price, max_price = int(df['price'].min()), int(df['price'].max())
price_range = st.sidebar.slider("Select Price Range", min_value=min_price, max_value=max_price, value=(min_price, max_price))

min_stars, max_stars = int(df['stars'].min()), int(df['stars'].max())
stars = st.sidebar.slider("Select Star Rating", min_value=min_stars, max_value=max_stars, value=(min_stars, max_stars))

# --- Apply Filters ---
filtered_df = df[
    (df['category'].isin(categories)) &
    (df['price'] >= price_range[0]) & (df['price'] <= price_range[1]) &
    (df['stars'] >= stars[0]) & (df['stars'] <= stars[1])
]

# --- Overview Stats ---
st.subheader("📊 Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Books", len(filtered_df))
col2.metric("Avg. Price", f"${filtered_df['price'].mean():.2f}")
col3.metric("Avg. Rating", f"{filtered_df['stars'].mean():.2f} ⭐")

# --- Bar Chart: Books by Category ---
st.subheader("📈 Number of Books by Category")
cat_count = filtered_df['category'].value_counts()
fig1, ax1 = plt.subplots()
cat_count.plot(kind='bar', color='skyblue', ax=ax1)
plt.xticks(rotation=45)
plt.ylabel("Number of Books")
plt.tight_layout()
st.pyplot(fig1)

# --- Histogram: Price Distribution ---
st.subheader("💵 Price Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df['price'], kde=True, bins=20, ax=ax2, color='salmon')
plt.xlabel("Price")
plt.ylabel("Count")
plt.tight_layout()
st.pyplot(fig2)

# --- Histogram: Ratings Distribution ---
st.subheader("⭐ Rating Distribution")
fig3, ax3 = plt.subplots()
sns.countplot(data=filtered_df, x='stars', palette='viridis', ax=ax3)
plt.xlabel("Stars")
plt.ylabel("Count")
plt.tight_layout()
st.pyplot(fig3)

# --- Top Rated Books ---
st.subheader("🏆 Top Rated Books")
top_books = filtered_df.sort_values(by=["stars", "price"], ascending=[False, True]).head(10)
for _, row in top_books.iterrows():
    st.markdown(f"**📘 {row['title']}**")
    st.markdown(f"- ⭐ {row['stars']} stars | 💲 {row['price']} | 📦 {row['availability']} in stock")
    st.markdown(f"- [🔗 View on Website]({row['url']})")
    st.markdown("---")

# --- Raw Data Table ---
st.subheader("📄 View Raw Data")
with st.expander("Show Data Table"):
    st.dataframe(filtered_df.reset_index(drop=True))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Netflix Data Dashboard")

df = pd.read_csv("netflix_titles.csv")

st.write("Dataset Preview")
st.dataframe(df.head())
total_titles = len(df)
movies = len(df[df["type"] == "Movie"])
tv_shows = len(df[df["type"] == "TV Show"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Titles", total_titles)

with col2:
    st.metric("Movies", movies)

with col3:
    st.metric("TV Shows", tv_shows)
    type_count = df["type"].value_counts()

fig, ax = plt.subplots()

type_count.plot(kind="bar", ax=ax)

ax.set_title("Movies vs TV Shows")

st.pyplot(fig)
country_count = (
    df["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .value_counts()
    .head(10)
)

fig, ax = plt.subplots()

country_count.plot(kind="bar", ax=ax)

ax.set_title("Top 10 Countries by Content")

st.pyplot(fig)
year_count = df["release_year"].value_counts().sort_index()

fig, ax = plt.subplots()

year_count.plot(kind="line", ax=ax)

ax.set_title("Content Released by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Titles")

st.pyplot(fig)
rating_count = df["rating"].value_counts().head(10)

fig, ax = plt.subplots()

rating_count.plot(kind="bar", ax=ax)

ax.set_title("Top Ratings Distribution")
ax.set_xlabel("Rating")
ax.set_ylabel("Count")

st.pyplot(fig)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def load_data():
    df = pd.read_csv('data/netflix_titles.csv')
    return df

st.set_page_config(
    layout='wide',
    page_title='Netflix Analysis Dashboard',
    page_icon='🎬'
)
st.title('Netflix and Chill')
st.subheader('Watch the best shows around the world')
with st.spinner('Loading data...'):
    df = load_data()
st.success('Netflix dataset loaded')

c1, c2, c3 = st. columns(3)
c1.header('Raw Netflix Dataset')
c1.dataframe(df)
c2.header('Statistical Summary')
c2.dataframe(df.describe())
c2.info('Display the Statistical Summary of the numerical values')
c3.header('Columns')
c3.write(", ".join(df.columns.tolist()))

c1, c2, c3 = st.columns(3)
c1.image('images/netflix_logo.png', use_column_width=True)
df_type = df['type'].value_counts()
c2.dataframe(df_type, use_container_width=True)
fig = px.pie(df_type, values=df_type.values,
             names=df_type.index, title='Netflix based on region')
c3.plotly_chart(fig, use_container_width=True)

num_cols = df.select_dtypes(include=np.number).columns.tolist()
cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()

c1, c2 = st.columns(2)
c1.header("2d Scatter Plot")
c1.subheader("Select x and Y to plot")
x = c1.selectbox("X", num_cols, key='Scatter1')
y = c1.selectbox("Y", num_cols, key='Scatter2')
color = c1.selectbox("color", cat_cols, key='Scatter3')
fig = px.scatter(df, x=x, y=y, color=color)
c1.plotly_chart(fig, use_container_width=True)
c2.header("3D Scatter plot")
c2.subheader("Select X,Y and Z to plot")
x = c2.selectbox("X", num_cols, key='Scatter3D_1')
y = c2.selectbox("Y", num_cols, key='Scatter3D_2')
z = c2.selectbox("Z", num_cols, key='scatter3d_3')
fig = px.scatter_3d(df, x=x, y=y, z=z)
c2.plotly_chart(fig, use_container_width=True)
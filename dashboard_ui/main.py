# import libraries

import streamlit as st # ui
import pandas as pd # analysis
import numpy as np # numerical analysis
import plotly.express as px # interactive graph

# run app
# open cmf (ctrl + j) in vs code
# run these commands:
# cd folder_name
#   streamlit run main.py
# load dataset
def load_data():
    df = pd.read_csv('data/pokemon.csv', index_col=0)
    return df

# add ui elements
st.set_page_config(
    layout='wide',
    page_title='pokemon Analysis Dashboard',
    page_icon="🍔"
)
st.title('Pokemon Analysis Dashboard')
st.subheader('Gotta Catch Them All')
with st.spinner("loading data..."):
    df =load_data()
st.success("pokemon Dataset Loaded!")

# Make interactive graphs
c1, c2, c3 = st.columns(3)
c1.header("Raw Dataset")
c1.dataframe(df)
c2.header("Statistical Summary")
c2.dataframe(df.describe())
c2.info("Display the Statistical Summary of the numerical value")
c3.header("Columns")
c3.write(", ".join(df.columns.tolist())) 

c1, c2, c3 = st.columns(3)
c1.image('images/pokemon22.jpg', use_column_width=True)
df_type_1 = df['Type_1'].value_counts()
c2.dataframe(df_type_1, use_container_width=True)

fig = px.pie(df_type_1, values=df_type_1.values,
             names=df_type_1.index, title='Pokemon Types')
c3.plotly_chart(fig, use_container_width=True)

# scatter plot
num_cols = df.select_dtypes(include=np.number).columns.tolist()
cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()
c1, c2 = st.columns(2)
c1.header("2D Scatter Plot")
c1.subheader("Select X and y to plot")
x = c1.selectbox("X", num_cols, key='scatter1')
y = c1.selectbox("Y", num_cols, key='scatter2')
color = c1.selectbox("color", cat_cols, key='scatter3')
fig = px.scatter(df, x=x, y=y, color=color)
c1.plotly_chart(fig, use_container_width=True)

c2.header('3D Scatter plot')
c2.subheader('select X, Y and Z to plot')
x = c2.selectbox("X", num_cols, key='scatter3d_1')
y = c2.selectbox("Y", num_cols, key='scatter3d_2')
z = c2.selectbox("Z", num_cols, key='scatter3d_3')
fig = px.scatter_3d(df, x=x, y=y, z=z,)
c2.plotly_chart(fig, use_container_width=True)
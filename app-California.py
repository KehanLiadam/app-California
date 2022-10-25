import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990)')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
Housing_filter = st.slider('Minimal Median House Price', 0, 500001, 200000)  # min, max, default

# create a multi select
ocean_proximity_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
    df.ocean_proximity.unique())  # defaults




#Display a radio button widget.
genre = st.sidebar.radio(
    "Choose the income level",
    ('Low', 'Medium', 'High'))

if genre == 'Low':
   df = df[df.median_income<=2.5]
elif genre == 'Medium':
   df = df[(df.median_income> 2.5) & (df.median_income< 4.5)]
else:
    genre == 'High'
    df = df[df.median_income> 4.5]
   
df = df[df.median_house_value <= Housing_filter]
df = df[df.ocean_proximity.isin(ocean_proximity_filter)]
# show on map
st.subheader('See more filters in the sidebar:')
st.map(df)


# show dataframe
fig, ax = plt.subplots(figsize=(5,5))
median_house_value=df.median_house_value
df.median_house_value.hist(bins=50)
st.pyplot(fig)




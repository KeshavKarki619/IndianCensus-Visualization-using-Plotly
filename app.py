#importing required libraries
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout= 'wide', page_title="India's data")

df = pd.read_csv("India.csv")

list_of_states =list(df['State'].unique())
list_of_states.insert(0,'Overall India')
list_of_states.insert(0,'select_one')


st.sidebar.title("Indias's census survey data")

selected_state =st.sidebar.selectbox('select a state',list_of_states)

primary_list = st.sidebar.selectbox("select primary parameter",  sorted(list(df.columns[5:]))) 
secondary_list = st.sidebar.selectbox("select secondary parameter",sorted(list(df.columns[5:])))

plot = st.sidebar.button('Plot Graph')


#Note:
if plot:
    if selected_state == 'Overall India':
        st.title("India's census - 2011 ")
        st.text('text represent primary parameter')
        st.text('color represent secondary parameter')

        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
        size = primary_list ,color=secondary_list,
        zoom=3.5,size_max=20,
        mapbox_style='carto-positron', 
        width=2000, height=700,
        hover_name='District'
        )

        st.plotly_chart(fig, use_container_width=True)
        
    else:
        st.title("India's census - 2011 ")
        st.text('text represent primary parameter')
        st.text('color represent secondary parameter')
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',
        size = primary_list ,color=secondary_list,
        zoom=3.5,size_max=20,
        mapbox_style='carto-positron', 
        width=2000, height=800,
        hover_name='District'
        )

        st.plotly_chart(fig, use_container_width=True)
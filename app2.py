import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout= 'wide', page_title="India's data")

st.header("About the project")

# Initialize session state variables
if "selected_state" not in st.session_state:
    st.session_state.selected_state = None
if "primary_list" not in st.session_state:
    st.session_state.primary_list = None
if "secondary_list" not in st.session_state:
    st.session_state.secondary_list = None

# Add condition to check if any dropdown is selected
if st.session_state.selected_state or st.session_state.primary_list or st.session_state.secondary_list:
    pass
else:
    st.markdown(""" 
    ### In my project analyzing the 2011 Indian census survey, I used Plotly to create an interactive map of India with a dropdown feature that allowed users to select different states and parameters. By processing and cleaning the census data with Python, I was able to identify key differences across states, including variations in literacy rates, education levels, religion, sex ratio, and household characteristics.
    ### Through my analysis, I identified differences in religion across different states, with some states having a much higher proportion of Hindus, while others had a higher proportion of Muslims. I was also able to identify differences in male vs. female ratios for each state, with some states having more males than females, and vice versa. By selecting different parameters, I was able to uncover even more insights
    """)

df = pd.read_csv("India.csv")

list_of_states =list(df['State'].unique())
list_of_states.insert(0,'Overall India')
list_of_states.insert(0,'select_one')

#making select_one for both primary and secondary
list_selection = sorted(list(df.columns[5:]))
list_selection.insert(0,'Select_one')

st.sidebar.title("Indias's census survey data")

selected_state =st.sidebar.selectbox('select a state',list_of_states, key="selected_state")

primary_list = st.sidebar.selectbox("select primary parameter",  list_selection, key="primary_list") 

plot1 = st.sidebar.button('Plot graph for primary parameter')
secondary_list = st.sidebar.selectbox("select secondary parameter",list_selection, key="secondary_list")

# plot = st.sidebar.button('Plot graph')
plot2 = st.sidebar.button('Plot graph for secondary parameter')

st.sidebar.text("  ")
st.sidebar.text("  ")
st.sidebar.text("  ")

plot3 = st.sidebar.button('Plot graph for both parameter')


#Note:
if plot1:
    if selected_state == 'Overall India':
        st.title("India's census - 2011 ")
        st.text('text represent primary parameter')
        st.text('color represent secondary parameter')

        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
        size = primary_list ,
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
        size = primary_list,
        zoom=3.5,size_max=20,
        mapbox_style='carto-positron', 
        width=2000, height=800,
        hover_name='District'
        )
        st.plotly_chart(fig, use_container_width=True)

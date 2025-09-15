
import streamlit as st
import langchain_helper

st.title("Restaurant Recommendation App")
cuisine = st.sidebar.selectbox(
    "Select a cuisine", 
    ["Indian", "Italian", "Chinese", "Mexican", "Thai"]
)



if(cuisine):
    response = langchain_helper.recommend_restaurants_name_with_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(", ")
    st.write("Menu Items:")
    for item in menu_items:
        st.write("- " + item)

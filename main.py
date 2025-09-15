
import streamlit as st

st.title("Restaurant Recommendation App")
cuisine = st.sidebar.selectbox(
    "Select a cuisine", 
    ["Indian", "Italian", "Chinese", "Mexican", "Thai"]
)

def recommend_restaurants_name_with_items(cuisine):
    return {
        'restaurant_names': ['Iyer Idli'],
        'menu_items': ['Idli', 'Sambar', 'Vada']
    }

if(cuisine):
    response = recommend_restaurants_name_with_items(cuisine)
    st.header(response['restaurant_names'][0])
    menu_items = response['menu_items']
    st.write("Menu Items:")
    for item in menu_items:
        st.write("- " + item)

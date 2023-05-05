import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('BREAKFAST MENU')
streamlit.text('🥣 blueberry 3 & oatmeal')
streamlit.text('🥗 kale,spinach and ricket smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🍞🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


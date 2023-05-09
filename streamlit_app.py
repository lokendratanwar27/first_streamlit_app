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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# normalized the response through pandas 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the table on the page
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("the fruit load list contains:")
streamlit.text(my_data_row)

add_my_fruit = streamlit.text_input("What fruit would you like to add?")
if streamlit.button("Add Fruit"):
  if add_my_fruit:
    my_fruit_list.append(add_my_fruit)
    st.write("Thanks for adding " + add_my_fruit )
  else:
    st.write("Please enter a fruit to add to the list.")


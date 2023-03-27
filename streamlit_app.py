import streamlit
import pandas
# import requests
import snowflake.connector
# from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')
# connect to snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()
# put the dafta into a dataframe
df = pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I Can see what I am working with
# streamlit.write(df)
# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)
# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))
# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'
# use the option selected to go back and get all the info from the database
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where
color_or_style = '" + option + "';")
df2 = my_cur.fetchone()
streamlit.image(
df2[0],
width=400,
caption= product_caption
)
streamlit.write('Price: ', df2[1])
streamlit.write('Sizes Available: ',df2[2])
streamlit.write(df2[3])



# streamlit.title("My Parents New Heathy Diner")

# streamlit.header("Breakfast Favorites")
# streamlit.text("🥣 Omega 3 & Bluerberry Oatmeal")
# streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
# streamlit.text("🐔 Hard-Boiled Free-Range Egg")
# streamlit.text("🥑🍞 Avocadoo Toast")

# streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')

# # Let's put a pick list here so they can pick the fruit they want to include 
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]

# # Display the table on the page.
# streamlit.dataframe(fruits_to_show)



# streamlit.text(fruityvice_response)

# streamlit.header("Fruityvice Fruit Advice!")
# try:
#   fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#   if not fruit_choice:
#     streamlit.error("Please select a fruit to get information.")
#    else:
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     streamlit.dataframe(fruityvice_normalized)

# expect URLError as e:
#   streamlit.error()

# streamlit.stop()

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from fruit_load_list")
# my_data_rows = my_cur.fetchall()
# streamlit.text("The Fruit load list contains:")
# streamlit.text(my_data_rows)

# add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
# streamlit.write('The user entered ', add_my_fruit)

# my_cur.execute("insert into fruit_load_list values ('from streamlit')")

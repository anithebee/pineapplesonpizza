import streamlit as st
from PIL import Image

#page config

st.set_page_config(page_title="Pizza Bakery", page_icon = ":pizza:")
st.title("Papa's Pizzeria - Walmart Edition")
st.subheader(":chicken: :cheese_wedge: :olive: :pineapple: :pizza:")


st.header("Place Your Order")
#base pizza + intialize
number_of_pizzas  = st.number_input("How many pizzas do you want?", min_value = 0, step=1)
fornow1 = 0
fornow2 = 0
fornow3 = 0
fornow4 = 0
extracost = 0
if number_of_pizzas>10 and number_of_pizzas<50:
    st.write("Oh...wow- thats a lot of pizzas.")
if number_of_pizzas>50:
    st.write("Excuse me?")
cost_per_pizza = 3

#toppings
pepperoni = st.checkbox("Pepperoni (3 Coins)")
olives =st.checkbox("Olives (2 Coins).")
doublecheese =st.checkbox("Double Cheese (4 Coins)")
chicken = st.checkbox("Chicken (6 Coins)")
pineapple = st.checkbox("Pineapple (2 Coins)")

#choices
choices = []
extracostlist = []
if pepperoni:
     choices.append('Pepperoni')
     extracostlist.append(3)
     st.write("pepperoni is hands down the best topping.")
if olives:
     choices.append("Olive-Topped")
     extracostlist.append(2)
     st.write("olives are respectable.")
if doublecheese:
     choices.append("Double Cheese")
     extracostlist.append(4)
     st.write("double cheese? mid topping but ok you do you.")
if chicken:
     choices.append("Chicken")
     extracostlist.append(6)
     st.write("chicken is a safe option, good choice.")
if pineapple:
     choices.append("Pineapple")
     extracostlist.append(2)
     st.write("YES YES YES DONT LISTEN TO THOSE HATERS PINEAPPLE IS SUPREME!!!!")
	

extracost = sum(extracostlist)

#bill
toppingslist = ' '.join(choices)
if number_of_pizzas>1:
    st.write(number_of_pizzas, toppingslist ," Pizzas coming right up!")
if number_of_pizzas==1 and len(choices)>=1:
    st.write(number_of_pizzas, toppingslist ," Pizza coming right up!")

if  len(choices)==0 and number_of_pizzas>1:
    st.write(number_of_pizzas, " Margherita Pizzas coming right up!")
if len(choices)==0 and number_of_pizzas==1:
    st.write(number_of_pizzas, " Margherita Pizza coming right up!")


st.subheader("Your Bill :money_with_wings:")
st.write("--->Base Pizza Price: 3")
for x in range(len(choices)):
    st.write("--->Topping: ", choices[x], ", Price: ", extracostlist[x])

st.write("--->Total Base Price: ", cost_per_pizza + extracost)
st.write("--->Quantity: ", number_of_pizzas)

subtotal = number_of_pizzas * (cost_per_pizza + extracost)
st.write("Subtotal: ", subtotal)
tax_rate = 0.08
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax
fornow3 =  st.write("Total (including tax): ", total)
fornow4 = st.write("This includes ", subtotal, " coins for the food and  ", sales_tax, " coins in sales tax.")



    

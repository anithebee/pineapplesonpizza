import streamlit as st

#page config

st.set_page_config(page_title="Pizza Bakery", page_icon = ":pizza:")
st.title("Papa's Pizzeria - Walmart Edition")
st.header("Menu || Plain Pizzas cost 3 coins.")
st.subheader("Toppings")
st.subheader(":chicken: :cheese_wedge: :olive: :pineapple: :pizza:")
st.write("(1) Pepperoni costs 3 coins.")
st.write("(2) Olives cost 2 coins.")
st.write("(3) Double Cheese costs 4 coins.")
st.write("(4) Chicken costs 6 coins.")
st.write("(5) Pineapple costs 2 coins.")
st.header("Place Your Order")

#base pizza
number_of_pizzas  = st.number_input("How many pizzas do you want?", min_value = 0, step=1)
fornow1 = 0
fornow2 = 0
fornow3 = 0
fornow4 = 0
if number_of_pizzas>10 and number_of_pizzas<50:
    st.write("Oh...wow- thats a lot of pizzas.")
if number_of_pizzas>50:
    st.write("Excuse me?")

#initialize
toppingsname = {0:"Margherita", 1:"Pepperoni", 2:"Olive", 3:"Double Cheese", 4:"Chicken", 5:"Pineapple"}
toppingsprice = {0:0, 1:3, 2:2, 3:4, 4:6, 5:2}
choiceslist = []
extracostlist = []
cost_per_pizza = 3
toppingschoice = 0

number_of_toppings = st.number_input("How many toppings would you like? Take a look at our toppings menu and choose from 0-5!", min_value=0, max_value=5, step=1)
if number_of_pizzas==0:
    st.write("um...you want plain toppings?")

for x in range(0, number_of_toppings, 1):
    toppingschoice = st.number_input(f"Choose your topping from the menu, from 1-5 (Topping {x+1}).", min_value=1, max_value=5, step=1)
    choiceslist.append(toppingsname.get(toppingschoice))
    extracostlist.append(toppingsprice.get(toppingschoice))
    


#addcommentsdict
emptylist = []
for x in choiceslist:
    if x not in emptylist:
        emptylist.append(x)

#bill
choices = ' '.join(emptylist)
if number_of_pizzas>1:
    st.write(number_of_pizzas, choices ," Pizzas coming right up!")
if number_of_pizzas==1 and number_of_toppings>=1:
    st.write(number_of_pizzas, choices ," Pizza coming right up!")

if number_of_toppings==0 and number_of_pizzas>1:
    st.write(number_of_pizzas, " Margherita Pizzas coming right up!")
if number_of_toppings==0 and number_of_pizzas==1:
    st.write(number_of_pizzas, " Margherita Pizza coming right up!")


st.subheader("Your Bill :money_with_wings:")
st.write("--->Base Pizza Price: 3")
for x in range(len(choiceslist)):
    st.write("--->Topping: ", choiceslist[x], ", Price: ", extracostlist[x])
extracost =0
for x in range(len(extracostlist)):
    extracost = extracost + extracostlist[x]

if toppingschoice!=0:
    st.write("--->Total Base Price: ", cost_per_pizza + extracost)
    st.write("--->Quantity: ", number_of_pizzas)

if toppingschoice != 0:
    subtotal = number_of_pizzas * (cost_per_pizza + extracost)
    st.write("Subtotal: ", subtotal)
    tax_rate = 0.08
    sales_tax = subtotal * tax_rate
    total = subtotal + sales_tax
    fornow3 =  st.write("Total (including tax): ", total)
    fornow4 = st.write("This includes ", subtotal, " coins for the food and  ", sales_tax, " coins in sales tax.")

if toppingschoice == 0:
    fornow1 = st.write("The cost before tax is: ", number_of_pizzas * cost_per_pizza)
    fornow2 = st.write("The total cost is ", (number_of_pizzas * cost_per_pizza)+ ((number_of_pizzas * cost_per_pizza) * 0.08))





    

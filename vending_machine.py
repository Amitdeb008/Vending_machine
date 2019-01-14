#***********************************************************************************************************************
#*********************************************VENDING MACHINE***********************************************************
#***********************************************************************************************************************
import time
print ("Welcome to the Vending Machine.")
# Asking the user how much money they wish to enter.
number_of_10p = int(input("How many 10 cents coins would you like to insert? "))
while number_of_10p < 0:
    number_of_10p = int(input("Please enter a positive number."))
number_of_25p = int(input("How many 25 cents coins would you like to insert? "))
while number_of_25p < 0:
    number_of_25p = int(input("Please enter a positive number."))
number_of_50p = int(input("How many 50 cents coins would you like to insert? "))
while number_of_50p < 0:
    number_of_50p = int(input("Please enter a positive number."))
number_of_100p = int(input("How many 1 dollar would you like to insert? "))
while number_of_100p < 0:
    number_of_100p = int(input("Please enter a positive number."))
# Creating a variable to store the total amount of money inserted into the vending machine.
change = round(((number_of_10p * 0.10) + (number_of_25p * 0.25) + (number_of_50p * 0.50) + (number_of_100p * 1.00)),2)
# Informing the user how much they have entered in total.
print ("\nIn total you have entered $", change)
time.sleep(2)
# Creating variables for the 6 drinks and their respective prices. 
drink_1 = "Coffee"
price_1 = 0.75
drink_2 = "Hot Chocolate"
price_2 = 2.50
drink_3 = "Cappuccino"
price_3 = 1.75
drink_4 = "Espresso"
price_4 = 2.35
drink_5 = "Caffe mocha"
price_5 = 2.65
drink_6 = "Boost"
price_6 = 2.15
# Creating variables to track the number of each items bought,
coffee_bought = 0
hot_chocolate_bought = 0
cappuccino_bought = 0
espresso_bought = 0
caffe_mocha_bought = 0
boosts_bought = 0
# Informing the user of the choices available and the prices that of each item.
print ("There are 6 drinks available to pick from;\n")
time.sleep(2)
print (" Item                   Costs")
print (" ----                   -----")
print (" {}         ----->  {} ".format(drink_1, price_1))
print (" {}  ----->  {} ".format(drink_2, price_2))
print (" {}     ----->  {} ".format(drink_3, price_3))
print (" {}       ----->  {} ".format(drink_4, price_4))
print (" {}    ----->  {} ".format(drink_5, price_5))
print (" {}          ----->  {} ".format(drink_6, price_6))
print ("")
# Asking the user to make a selection.
while change > 0:
    customer_choice = input("What would you like to buy? Type N when you are finished \n")
    if customer_choice == "Coffee" or customer_choice == "coffee" and change >= price_1:
        print ("You have chosen a", drink_1, "these cost", price_1, "each,")
        change = round((change - price_1),2)
        coffee_bought = (coffee_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Hot Chocolate" or customer_choice == "hot chocolate" and change >= price_2:
        print ("You have chosen a", drink_2, "these cost", price_2, "each,")
        change = round((change - price_2),2)
        hot_chocolate_bought = (hot_chocolate_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Cappuccino" or customer_choice == "cappuccino" and change >= price_3:
        print ("You have chosen a", drink_3, "these cost", price_3, "each,")
        change = round((change - price_3),2)
        cappuccino_bought = (cappuccino_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Espresso" or customer_choice == "espresso" and change >= price_4:
        print ("You have chosen a", drink_4, "these cost", price_4, "each,")
        change = round((change - price_4),2)
        espresso_ways_bought = (espresso_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Caffe mocha" or customer_choice == "caffe mocha" and change >= price_5:
        print ("You have chosen a", drink_5, "these cost", price_5, "each,")
        change = round((change - price_5),2)
        caffe_mocha_bought = (caffe_mocha_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "Boost" or customer_choice == "boost" and change >= price_6:
        print ("You have chosen a", drink_6, "these cost", price_6, "each,")
        change = round((change - price_6),2)
        boosts_bought = (boosts_bought + 1)
        print ("You have this much money remaining: $", change)
    elif customer_choice == "N" or customer_choice == "n":
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (coffee_bought, "x", drink_1)
        print (hot_chocolate_bought, "x", drink_2)
        print (cappuccino_bought, "x", drink_3)
        print (espresso_bought, "x", drink_4)
        print (caffe_mocha_bought, "x", drink_5)
        print (boosts_bought, "x", drink_6)
        print ("You have $", change, "remaining.")
        break
    elif change <= 0:
        print ("You have run out of money.")
        print ("\nHere is your transaction details:\n")
        print ("You purchased: ")
        print (coffee_bought, "x", drink_1)
        print (hot_chocolate_bought, "x", drink_2)
        print (cappuccino_bought, "x", drink_3)
        print (espresso_bought, "x", drink_4)
        print (caffe_mocha_bought, "x", drink_5)
        print (boosts_bought, "x", drink_6)
        break
    else:
        print ("There has been an error or you may not have enough credit.")

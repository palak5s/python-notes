# CALCULATOR PROGRAM
# operator = input("Enter an operator(+ - * /):")
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# if operator=="+":
#     result=num1+num2
#     print(result)
# elif operator=="-":
#      result=num1-num2
#      print(result)
# elif operator=="*":
#     result=num1*num2
#     print(result)
# elif operator=="/":
#     result=num1/num2
#     print(result)
# else:
#     print(f"{operator} is not a valid operator")

################################ WEIGHT CONVERTER ###################################
# weight=float(input("Enter your weight"))
# unit=input("Kilograms or Pounds? (K or L)")
# if unit=="K":
#     weight=weight*2.205
#     unit="Lbs"
#     print(f"Your weight is : {round(weight, 2)}{unit}")
# elif unit=="L":
#     weight=weight / 2.205
#     unit="Kgs"
#     print(f"Your weight is : {round(weight, 2)}{unit}")
# else:
#     print(f"{unit} was not valid")
############################## TEMPERATURE CONVERTER #############################
# unit=input("Is this temperature in celsius or Fahrenheit(C/F)")
# temp=float(input("Enter the temperature:"))
# if unit=='C':
#     temp=round((9*temp)/5+32,1)
#     print(f"The temperature in Fahrenheit is : {temp}°F")
# elif unit=="F":
#     temp=round((temp-32)*5/9)
#     print(f"The temperature in Celsius is : {temp}°C")
# else:
#     print(f"{unit} is an invalid unit of measurement")
################################## COMPOUND CALCULATOR #########################################################
principle = 0
rate = 0
time = 0
# while principle<=0:
#     principle=float(input("Enter the principle amount:"))
#     if principle<=0:
#         print("Principle can't be less than or equal to zero")
# print(principle)
# while rate<=0:
#     rate=float(input("Enter the rate amount:"))
#     if rate<=0:
#         print("rate can't be less than or equal to zero")
# print(rate)
# while time<=0:
#     time=float(input("Enter the  time amount:"))
#     if time<=0:
#         print("time can't be less than or equal to zero")
# print(time)
# compound_interest=principle * pow((1+rate/100),time)
# print(f"Balance after {time} years/s: ${compound_interest: .2f}")

# while True:
#     principle=float(input("Enter the principle amount:"))
#     if principle<0:
#         print("Principle can't be less than or equal to zero")
#     else:
#         break
# print(principle)
# while True:
#     rate=float(input("Enter the rate amount:"))
#     if rate<0:
#         print("rate can't be less than or equal to zero")
#
#     else:
#         break
# print(rate)
# while True:
#     time=float(input("Enter the  time amount:"))
#     if time<0:
#         print("time can't be less than or equal to zero")
#
#     else:
#         break
# print(time)
# compound_interest=principle * pow((1+rate/100),time)
# print(f"Balance after {time} years/s: ${compound_interest: .2f}")

######################################## COUNTDOWN TIME PROGRAM ###########################################################
#importing time module
# import time
#
# my_time = int(input("Enter time in seconds:"))
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x/60) % 60
#     hours = int(x/3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     #sleep function is used and inside the parenthesis the time in seconds for that time the program will sleep and works after
#     # print(x)
#     time.sleep(1)
# print("TIME'S UP!")
############################################ SHOPPING CART PROGRAM #######################################################################################
# foods=[]
# prices=[]
# total=0
# while True:
#     food= input("Enter a food to buy(qto quit): ")
#     if food.lower()=="q":
#         break
#     else:
#         price=float(input(f"Enter the price of a food {food}: $"))
#         foods.append(food)
#         prices.append(price)
#
# print("---YOUR CART-----")
# for food in foods:
#     # to
#     print(food,end=" ")
# for price in prices:
#     total+=price
# print(f"Your total is :${total}")


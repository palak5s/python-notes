# This is used as comment symbol in python
################################### INTRODUCTION #####################################
# print("hello")
# print("I am AI developer with full stack specialisation")
################################### VARIABLE ########################################
#Variable=A container for value(Str
#  ing, integer,float, boolean)
#         A variable behaves as if it was the value it contains
# A String is a series of characters
# first_name="Bro"
# food="pizza"
# email="Bro123@fake"
# print(first_name)
#### docstring
##################################### f-string #############################################################
#f-string : it is a formatted string and we can write expression between placeholder{} this can refer to variables or literal values. We use f before double quote or triple quote.
# print(f"Hello {first_name}")
# print(f"you like{food}")
# print(f"your email is :{email}")

################################ INTEGER #####################################################################
# An Integer is a whole number
# age=25
# quantity=3
# print(f"You are {age} years old")
# print(f"You are buying {quantity} items")
# num_of_students=30
# print(f"Your class has {num_of_students} students")
################################ FLOAT  ######################################################
# #Float
# price=10.9
# gpa=9.5
# distance=5.5
# print(f"The price is ${price}")
# print(f"My gpa is {gpa}")
# print(f"my school is {distance}km from my home")
############################ BOOLEAN #####################################
# #Boolean are binary either they are true or false
# is_student=False
# for_sale=True
# is_online=True
# if is_student:
#         print("You are student")
# else:
#         print("You are not a student")
#         if for_sale:
#             print("That item for sale")
#         else:
#             print("That item is Not available")
#             if is_online:
#                 print("You are online")
#             else:
#                 print("You are not online")
#################################### TYPECASTING #############################################################################
# #TypeCasting= the process of converting  a variable from one datatype to another str(), int(), float(), bool()
# name="bro code"
# age=25
# gpa=3.3
# is_student=True
# print(type(is_student)) #type() function is used to define the datatype of variable
# gpa=int(gpa)
# print(gpa)
# age=bool(age)#by default it prints true
# print(age)
# # is_student=str(is_student)
# # print(is_student)
#
# is_student=int(is_student)
# print(is_student)
# age=str(age)
# age+="1"
# print(age)
#
# print(type(age))
# name=bool(name)
# print(name)
########################################### INPUT ################################################################
#input()=A function that prompts the user to enter data Returns  the entered data as a string
# name=input("What is your name?:")
# age= int(input("How old are you?"))
# # age=int(age)
# age=age+1
# print(f"Hello{name}!")
# print("HAPPY BIRTHDAY")
# print(f"Your are {age} years old")
######################Exercise1 Rectangle Area Calc######################
# length= int(input("Enter length of Rectangle:"))
# width=int(input("Enter width of Rectangle:"))
# area= length*width
# print(f"The area is {area}")
############################## Exercise:2  Shopping Cart Program#######################################
# item=input("What item would you like to buy?")
# price=float(input("What is the price?:"))
# quantity=int(input("How may would you like?:"))
# total=price*quantity
# print(f"You have bought {quantity}X{item}/s")
# print(f"Your total is:{total}")
######################### Madlibs game ######################################
#Word game where you create a story
# by filling in blanks with random words
# adjective1=str(input("Enter an adjective(description):"))
# noun1=str(input("Enter a noun (person,place,thing):"))
# verb1=str(input("Enter a verb"))
# adjective2=str(input("Enter an adjective (description):"))
# adjective3=str(input("Enter an adjective (description):"))
# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit,I saw a{noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")
################################### Arithmetic Operation and Math function ########################################################
friends=5
# friends=friends+1
#friends+= 1 an argument assignment operator\
# friends=friends-2
# friends -= 2
# friends=friends*3
# friends*=3
# friends=friends/2
# friends/=2
# friends=friends**2
# friends ** = 2
# friends=friends%3
# friends %=2
# print(friends)
#################################### built-in math function ##########################################################
# x=3.14
# y=-4
# z=5
# result= round(x)
# result=abs(y)
# result=pow(z,2)
# result=max(x,y,z)
# result=min(x,y,z)
# print(result)
########################### Importing Math Function #####################################################
import math
# x=9.1
# print(math.pi)
# print(math.e)
# result=math.sqrt(x)
#### CEIL() That is ceil function returns an integer that is just greater than a certain rational value.
# Ceil function is used in situations where exact integer values are required which is just greater than or equal to the given value.
# result=math.ceil(x)
################ FLOOR() That is floor function returns an integer that is just lesser than a certain rational value.
# Floor function is used in situations where exact integer values are required which is just lesser than or equal to the given value.
# result=math.floor(x)
# print(result)
###################### Exercise:3#####################################
# import math
# radius= float(input("Enter the radius of a circle"))
# circumference=2*math.pi*radius
# print(f"The circumference is:{round(circumference,2)}cm")
######################### Exercise:4 #################################
# import math
# radius=float(input("Enter radius of a circle:"))
# area=math.pi*pow(radius,2)
# print(f"Area of circle is: {round(area,3)}cm^
###################### Exercise:5 ###################################
# import math
# height=float(input("Enter the height of right angled triangle:"))
# base=float(input("Enter the base of right angled triangle:"))
# hypotenuse= math.sqrt(pow(height,2)+pow(base,2))
# print(f"Hypotenuse of right angled triangle is {hypotenuse}cm")






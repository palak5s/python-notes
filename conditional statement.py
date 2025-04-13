# if= Do some code only IF some condition is True
# Else do something else
# age=int(input("Enter your age"))
# if age>=18:
#     print("You are now signed up")
# elif age<0:
#     print("You haven't born yet!")
# elif age>100:
#     print("You are too old to sign up")
# else:
#     print("You must be 18+ to sign up")
####################################### Exercise:6
# response=input("would you like food? (Y/N)")
# if response=="Y":
#     print("Have some food")
# else:
#     print("No food for you")
########################Exercise:7
# name=input("Enter your name:")
# if name=="":
#     print("You did not ty"
#           "pe in your name!")
# else:
#     print(f"Hello{name}")
########################Exercise:8
# for_sale=False
# if for_sale:
#     print("this item if for sale")
# else:
#     print("the user is offline")
################################################ LOGICAL OPERATOR ##########################################################
# logical operators= evaluate multiple conditions (or,and,not)
#                                          or= at least one condition must be True
#                                         and= both conditions must be True
#                                         not= inverts the condition (not False, not True)
# temp=0
# is_raining=False
# if temp > 35 or temp< 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")
# temp=25
# is_sunny= False
# if temp >= 28 and is_sunny:
#     print('It is Hot Outside')
#     print('It is SUNNY☀')
# elif temp <= 0 and is_sunny:
#     print('It is cold outside')
#     print('It is SUNNY☀')
# elif 0 < temp <=28 and not is_sunny:
#     print("It is a warm inside")
# else:
#     print("It is a mild day")
##################################### CONDITIONAL EXPRESSION #####################################
# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of the two values based on a condition
#                          X if condition else Y

# num=6
# a=7
# b=8
# age=34
# temperature=90
# user_role="admin"
# print("Positive" if num > 0 else "Negative")
# result= "EVEN" if num % 2 == 0 else "ODD"
# max_num= a if  a > b else b
# min_num = a if a < b else b
#
# print(max_num)
# print(min_num)
# status = "Adult" if age >= 18 else "child"
# weather="Hot" if temperature > 20 else  "cold"
# access_level = "Full access" if user_role == "adimin" else "limited acess"
# print(access_level)
############################## STRING METHODS ########################################################
# name =input("Enter your full name:")
# result= len(name)
# result = name.find("s")
# result=name.rfind("q")
# result=name.capitalize()
# result=name.upper()
# name=name.upper()
# name=name.lower()
# result=name.isdigit()
# result=name.isalpha()
# phone_number=input("Enter your phone number:")
# result=phone_number.count("-")
# phone_number=phone_number.replace("-"," ")
# print(help(str))

# print(phone_number)
#Validate user input experience
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits
# username=input("Enter a username")
# if len(username)>12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ")== -1:
#     print("your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers  ")
# else:
#     print(f"welcome{username}")
#indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]
# credit_number="1234-5678-9012-3456"
# print(credit_number[1])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-4])
# print(credit_number[::2])
# print(credit_number[-4:])
# print(credit_number[::-1])
#################################### FORMAT SPECIFIERS  #######################################################
#format specifiers ={ value:flags} format a value based on what flags are inserted
#.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place a sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator
# price1=300000.14159
# price2=-98700.65
# price3=120000.34
# this format specifier take 10 index
# print(f"Price 1 is ${price1 : 10}")
# print(f"Price 1 is ${price2 : 10}")
# print(f"Price 1 is ${price3 : 10}")
#this format specifiers take 10 index but replace the starting index with 0's
# print(f"Price 1 is ${price1 : 10}")
# print(f"Price 1 is ${price2 : 10}")
# print(f"Price 1 is ${price3 : 10}")
# for center align
# print(f"Price 1 is ${price1 : ^10}")
# print(f"Price 1 is ${price2 : ^10}")
# print(f"Price 1 is ${price3 : ^10}")
# print(f"Price 1 is ${price1 :+}")
# print(f"Price 1 is ${price2 :+}")
# print(f"Price 1 is ${price3 :+}")
# print(f"Price 1 is ${price1 : 10}")
# print(f"Price 1 is ${price2 : 10}")
# print(f"Price 1 is ${price3 : 10}")
# print(f"Price 1 is ${price1:,}")
# print(f"Price 1 is ${price2:,}")
# print(f"Price 1 is ${price3:,}")


# dictionary = a collection of {key:value} pairs ordered and changeable. NO duplicates.
# capitals = {"USA":"Washington DC",
# "India":"New Delhi",
# "China": "Beijing", "Russia": "Moscow"}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")
########### With update function we can add new key value pair in dictionary
# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Deteroit"})
# capitals.pop("China")
###Will pop an item from the last of the dictionary
# capitals.popitem()
# # capitals.clear()
# print(capitals)
# keys = capitals.keys()
# print(keys)
# for key in capitals.keys():
#     print(key)
# values = capitals.values()
# print(values)
# for value in capitals.values():
#     print(value)
################# print as 2D tupple
# items = capitals.items()
# print(items)
# for key,values in capitals.items():
#     print(f"{key}:{values}")
############################# CONCESSION STAND PROGRAM #####################
# menu = {"pizza":3.00,
#         "nachos":4.50,
#         "popcorn":6.00,
#         "fries":2.50,
#         "chips":1.00,
#         "pretzel":3.50,
#         "soda":3.00,
#         "lemonade":4.25}
# cart = []
# total =0
# print("______________MENU__________________")
# for key,value in menu.items():
#     print(f"{key:10}:${value:.2f}")
# print("___________________________")
# while True:
#         food = input("select an item (q to quit):").lower()
#         if food=="q":
#                 break
#         elif menu.get(food) is not None:
#                 cart.append(food)
#
# for food in cart:
#         total =  total+ menu.get(food)
#         print(food,end=" ")
# print()
# print(f"Total is : ${total:.2f}")
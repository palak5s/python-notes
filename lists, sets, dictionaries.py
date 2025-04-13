#collection = single "variable" used to  store multiple values
# List = [] ordered and changeable. Duplicate Ok
# Set = {} unordered and immutable, but Add/ Remove OK. NO duplicates
 # Tuple = () ordered and unchangeable . Duplicate OK. FASTER than lists
 ############################### LISTS ####################################################################
# fruits = ["apple", "orange", "banana", "coconut"]
# print(fruits[0:3])
# print(fruits[::3])
# print(fruits[::-1])
# for fruit in fruits:
#     print(fruit)
# # print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits) to check if item of the list exist or not
# replace the item at that  index
# fruits[0]= "pineapple"
# fruits.append("pineapple") to add the elements at the end of the list
# fruits.remove("apple") to remove the item
# # fruits.insert(0,"chio") used to insert the element at particular index
# fruits.sort() sort the element according to the alphabetic order
# # fruits.reverse()
# fruits.clear() to empty the string
# print(fruits.index("apple"))
# print(fruits.count("banana"))
# print(fruits)
######################################### SETS ########################################################################
# fruits = {"apple", "orange", "banana", "coconut", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# print(fruits[0]) set is an unordered so we can't access the element
# fruits.add("lemon") add element at the last of the set
# fruits.pop() it removes the any random item
# fruits.remove("apple")
# fruits.clear()
# print(fruits)
######################################## TUPLE ############################################
# fruits=("apple","orange","banana","coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)
# # print(fruits.index("apple"))
# print(fruits.count("coconut"))
# for fruit in fruits:
#     print(fruit)
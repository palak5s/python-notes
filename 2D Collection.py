# # fruits = ["apple","orange","banana","coconut"]
# # vegetables =["celery","carrots","potatoes"]
# # meats =["chicken","fish","turkey"]
# # 2D collection can be of tupple of tupple ,list of list, sets of sets
# # groceries =[["apple","orange","banana","coconut"],["celery","carrots","potatoes"],["chicken","fish","turkey"]]
# # for collection in groceries:
# # # print(collection)
# # # print(groceries)
# #     for food in collection:
# #          print(food, end=" ")
# #     print()
# # ############################## 2Dimensional Keypad ######################################
# # num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
# # for row in num_pad:
# #     for num in row:
# #         print(num,end=" ")
# #     print()
# ################################PYTHON QUIZ GAME ##################################################
# questions =("How many elements are in the periodic table?:","Which animal lays the largest eggs?:", "what is the most abundant gas in Earth's atomsphere?:","How many bones are in human body?:", "Which planet in the solar system is the hottest?:")
# options =(("A.116","B.117","C.118"),("A.Whale","B.Ostrich","C.Crocodile"),("A.Nitrogen","B.Oxygen","C.Helium"),("A.206","B.207","C.208"),("A.Mercury","B.,Venus","C.Earth",))
# answers = ("C","B","A","A","A")
# guesses =[]
# score = 0
# question_num = 0
# for question in questions:
#     print("___________________")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess =input("Enter A,B,C:").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         score += 1
#         print("CORRECT")
#     else:
#         print("INCORRECT")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num +=1
# print("____________________")
# print("     RESULTS          ")
# print("________________________")
# print("answers:",end=" ")
# for answer in answers:
#     print(answer,end=" ")
# print()
# print("guesses: ",end=" ")
# for guess in guesses:
#     print(guess,end=" ")
# print()
# score =int (score/len(questions)*100)
# print(f"Your score is : {score}%")
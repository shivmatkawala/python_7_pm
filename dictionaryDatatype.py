# myname = "Shivkumar"
# print(myname)


# grocerry = ["Oil", "Sugar", 'Maida Pindi', "Soap", "Lentels"]
# print(grocerry)


# ahemad = {
#     'height' : 5,
#     'weight': 100,
#     'color': 'Whetish',
# }

# ----------------------------------------

# dict2 = {
#     1:1,
#     2:4,
#     3:9,
#     4:16,
#     5:25
# }
# print(dict2)
# print(type(dict2))

# print("-------------------------------")

# dict3 = dict()
# print(dict3)
# print(type(dict3))

# print("-------------------------------")

# dict4 = {}
# print(dict4)
# print(type(dict4))

# print("-------------------------------")

# dict5 = {
#     "fruit1": "Apple",
#     "fruit2": "Grapes",
#     "fruit3": "Banana",
#     "fruit4": "Papaya"
# }

# print(dict5)
# print(type(dict5))


# print("-------------------------------")

# dict6 = dict(mla="arvind", sachin="cricketer", shiva="very very common-man")
# print(dict6)
# print(type(dict6))

# print("-------------------------------")

husbands = ["virat", "ramcharan", "NTR", "Allu Arjun", "Jai Balayya", "Mahesh Babu"]
wives = ["Anushka", "Upasana", "Pranathi", "Sneha", "XXXX", "Namrtha"]

dict7 = dict(zip(husbands, wives))
# print(dict7)
# print(type(dict7))

# print("-------------------------------")

# students = ["Shalini", "Uma", "Neha", "Kiran", "Sameer", "Aehmad", "Vijay", "Mirza", "KTR"]

# dict8 = dict.fromkeys(students, "Samantha")

# print(dict8)
# print(type(dict8))


# print("-------------------------------")

# dict9 = dict([("Laila", "Majnu"), ("Heer", "Ranjha"), ("Arjun", "Preethi"), ("Romeo", "Juleat"), ("Soni", "Mehwal")])
# print(dict9)
# print(type(dict9))


#------------------------------------------------

# ACESSING ELEMENTS

# print(dict7)

# print ramus wife name

# print(dict7['ramcharan'])

# print(dict7['Allu Arjun'])

# # print(dict7['Sneha'])

# # print(dict7[3])

# # all keys from dicct7

# print(dict7.keys())
# print(type(dict7.keys()))  #<class 'dict_keys'>


# # all values
# print(dict7.values())
# print(type(dict7.values())) #<class 'dict_values'>

# all items

print(dict7.items())
print(type(dict7.items()))  #<class 'dict_items'>


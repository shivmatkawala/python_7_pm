# SET :-

# set is a collection
# set is is collection unique elements
# set is mutable
# set is unordered
# doest allow duplicates
# it is partially heterogeneous.
# it doesnt support indexing.

# How to intialize /  create a set:-

# set1 = {1,}
# print(set1)
# print(type(set1))

# set2 = set([1, 2, 3, 4, 5])
# print(set2)
# print(type(set2))

# set3 = set((10, 20, 30, 40))
# print(set3)
# print(type(set3))

# set4 = set({90, 80, 70, 60})
# print(set4)
# print(type(set4))


# set5 = set("APPLE")
# print(set5)
# print(type(set5))


# Membership Operator:-
    # in
    # not in
# set100 = {"A", 12, 34.5, 67, False, ('a', 'c', 100, True)}

# print("A" in set100)
# print("A".lower() in set100)
# print(0.000000 in set100)
# print(120 not in set100)
# print(1 in set100)




# ADDING ELEMENTS TO THE SET:-

# set420 = {12, 23, 34, 45,  56}

# set420.add(67)
# print(set420)


# set420.add("BABOON".title())
# print(set420)

# set420.add(False)
# print(set420)
# set420.add((1, 2, 3))
# print(set420)

# set420 = {12, 23, 34, 45, 56, "a", 65}
# set420.remove(False)
# set420.remove(34)
# set420.remove(9*5)
# set420.remove((True + True) * 6)
# print(set420)
# set420.remove(chr(97))
# set420.remove(ord('A'))
# print(set420)

#######################################

set143 = {"A", 'B', 6, 7.5, (1, 2, 3), "Hello"}

# print(set143)
# print(type(set143))

# # clear()
# set143.clear()
# print(set143)
# print(type(set143))


# set143 = {"A", 'B', 6, 7.5, (1, 2, 3), "Hello"}

# set143.update("AMONIA")
# print(set143)

# set143.update([90, 89, 78])
# print(set143)


# set143.update((True, False, 0, 1, (1, 2, 0)))
# print((set143))


# set143.update({100, 200, 300, {'I', "A", "O"}})    # No possible
# print(set143)


# set143 = {"A", 'B', 6, 7.5, (1, 2, 3), "Hello"}

# set143.pop()
# print(set143)



###################################################

# Set Operations:-
# set1 =  {1, 2, 3}
# set2 = {3, 4, 5}

# union
# set3 = set1 | set2
# print(set3)   #{1, 2, 3, 4, 5}

# # difference

# set1 =  {1, 2, 3}
# set2 = {3, 4, 5}

#     # set 1 - set2
# set4 = set1 - set2
# print(set4)

#     # set2 - set1
# set5 = set2 - set1
# print(set5) 
 
# # intersection
# set6 = set1 & set2
# print(set6)  #{3}

# # symmetric difference

# set7 = set1 ^ set2
# print(set7)   #{1, 2, 4, 5}

######################################################

set1 = {11, 22, 33, 44}
set2 = {99, 33, 10, 200}

# print(set1.isdisjoint(set2))
# set1.difference_update(set2)   # 99, 10, 200, 11, 22, 33, 44
# print(set1)

# set1.intersection_update(set2)
# print(set1)


# # is sbuset

# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5}
# s3 = {3, 4, 5}
# s4 = {9, 1, 2, 3}
# s5 = {3, 4, 5, 6, 7}


# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s3.issubset(s1))


# print(s5.issuperset(s2))
# print(s5.issuperset(s1))


s11 = {1, 2, 3, 4}
# s12 = {4, 5, 6, 7, 8}

# s11.symmetric_difference_update(s12)
# print(s11)


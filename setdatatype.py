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

set420 = {12, 23, 34, 45, 56, "a", 65}
# set420.remove(False)
# set420.remove(34)
# set420.remove(9*5)
# set420.remove((True + True) * 6)
# print(set420)
# set420.remove(chr(97))
set420.remove(ord('A'))

print(set420)


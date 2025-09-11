# Range:-

    # Immutable Sequence of Numbers:-
    # Generates Numbers on fly:-
    # Doesnt store numbers in memory
    # memory efficient
    # We use this datatype in loop.
    
# Initialize Range:-

# only single argument--> stop
# python takes default start --> 0
# python takes default step --> 1
# r1 = range(1)
# print(r1)   #range(0, 5)

# l1 = list(r1)
# print(l1)


# if gives two numbers as an argument,
# first number --> start
# last number --> stop
# python takes step as a default --> 1

# r2 = range(5, 15)
# print(r2)
# t1 = tuple(r2)
# print(t1)


# if gives three arguments 
# first number --> start
# second number --> stop
# third number --> step

# r3 = range(2, 20, 5)
# # 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13 14, 15, 6, 17, 18, 19
# print(r3)

# s1 = set(r3)
# print(s1)



# ACCESSING ELEMENTS FROM RANGE:-

r4 = range(23, 6, -1)
print(r4)
# print(r4[0])
# print(r4[1])
# print(r4[2])
# print(r4[3])
# print(r4[4])
# print(r4[-1])
# print(r4[-2])
# print(r4[-3])

#----------------------------

# r5 = range(-34, 5, 2)
# print(len(r5))
# print(max(r5))
# print(min(r5))
# print(sum(r5) / len(r5))


# print(r5.count(2))

# print(r5.index(2))

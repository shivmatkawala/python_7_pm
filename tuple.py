# tuple:-
    # immutable
    # heterogeneous
    # ordered
    # indexed
    # used to store fix data.



# How to create / initialize tuple:-

# tup1 = (1, 2, True, 'Bangaram', 'Bujji', ['A', 'B', 0.5])
# print(tup1)
# print(type(tup1))   #<class 'tuple'>

# tup2 = tuple([1, 2, 3, 4, 5])
# print(tup2)
# print(type(tup2))

# tup3 = tuple((10, 'A', 5.5, False))
# print(tup3)
# print(type(tup3))

# tup4 = tuple({50, 60, 70,  'Priya'})
# print(tup4)
# print(type(tup4))

# tup5 = tuple('APPLE')
# print(tup5)
# print(type(tup5))


#################################

# t1 = (12, 23, 'SURESH', True, 5.5, [1, 2, 3])
# print(t1)

# positive indexing
# print(t1[0])
# print(t1[1])
# print(t1[2])

# negative indexing
# print(t1[-1])
# print(t1[-2])
# print(t1[-3])

# t1 = (12, 23, 'SURESH', True, 5.5, [1, 2, 3])

# Slicing
# print(t1[0:3:1])
# print(t1[-4:-1:1])
# print(t1[3:0:-1])


# t1 = (12, 23, 'SURESH', True, 5.5, [1, 2, 3])

# print(t1[2][2])
# print(t1[2][-1])
# print(t1[-1][1])


# In buillt methods
t1 = (12, 23, 'SURESH', True, 5.5, [1, 2, 3], 12, 8, 'g', False, 0, 1)

#count
# print(t1.count(12))
# print(t1.count(1))
# print(t1.count(False))


# index
# print(t1.index(5.5))
# print(t1.index('g'))


# concatination
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)

# Repitation

# t11 = (1, 2, 3)
# print
# (t11 * 3)



# Unpacking

# t100 = (12, 23, 45)
# a, b, c =  t100

# print(a)
# print(b)
# print(c)


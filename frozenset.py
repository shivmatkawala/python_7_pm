# Frozenset
    # same like set, but immutable.
    

# initialize set:-

# f_set1 = frozenset((1, 2, 3, 4,5 ,6, 7,8))
# print(f_set1)
# print(f_set1)  #<class 'frozenset'>

# print("------------------------------------------")

# f_set2 = frozenset(['A', 'B', 12, 34, 0, True, False])
# print(f_set2)
# print(type(f_set2))  #<class 'frozenset'>

# print("------------------------------------------")

# f_set3 = frozenset({12, "Imran Hashmi", False, '0', None, 0})
# print(f_set3)
# print(type(f_set3))


# print("------------------------------------------")

# # Membership Operators:-

# # f_set4 = frozenset([1, 2, 3, 4, 5])
# # print(4 in f_set4)
# # print(1 in f_set4)
# # print(10 not in f_set4)
# # print(11 in f_set4)


# # SET OPERATIONS:-

# s1 = frozenset([1, 2, 3, 4])
# s2 = frozenset([3, 4, 5, 6])

# # Union
# print(s1 | s2)

# # Intersection
# print(s1 & s2)

# # difference 
# print(s1 - s2)
# print(s2 - s1)


# # symmetric difference
# print(s1 ^ s2)


# OTHER OPERATIONS:-

# s3 = frozenset([1, 2, 3])  # subset
# s4 = frozenset([1, 2, 3, 4, 5 ,6])  # superset

# print(s3.issubset(s4))
# print(s4.issuperset(s3))

# print(s4.issubset(s4))
# print(s4.issuperset(s4))

# print(s3.issuperset(s4))


# dict1 = {
#    1:100,
#    's':'shalini',
#    None: 'Nothing',
#    True: 'Yes',
#    2.5: 'two point five',
# #    [1, 2, 3]: 'list', 
#    (0,9,8): 'tup',
# #    {1, 2, 3, 4}: 'set'
#     frozenset([1, 2, 3, 4]): 10,
# }

# print(dict1)


#  Union
s1 = frozenset([1, 2, 3, 4])
s2 = frozenset([3, 4, 5, 6])

# print(s1 | s2)

# print(s1.union(s2))  # same as above

#
# Intersection:

# print(s1 & s2)

# print(s1.intersection(s2))  # same as above

# difference:

# print(s1 - s2)

# print(s1.difference(s2))  # same as above

# print(s2 - s1)

# print(s2.difference(s1))  # same as above

# symmetric difference:

# print(s1 ^ s2)
# print(s1.symmetric_difference(s2))  # same as above

# print(s2 ^ s1)
# print(s2.symmetric_difference(s1))  # same as above


# print("------------------------------------------")

# OTHER OPERATIONS:-

# s3 = frozenset([1, 2, 3])  # subset
# s4 = frozenset([1, 2, 3, 4, 5 ,6])  # superset

# print(s3.issubset(s4))
# print(s4.issuperset(s3))
# print(s3.issuperset(s4))
# print(s4.issubset(s3))


f1 = frozenset([1, 2, 3, 4, 5])

print(max(f1))
print(min(f1))
print(sum(f1))

def avg(fset):
    return sum(fset) / len(fset)

print(avg(f1))

import math

print(math.prod(f1))

print(len(f1))


print(sorted(f1, reverse=True))

import statistics

print(statistics.mean(f1))
print(statistics.median(f1))
print(statistics.mode(f1))  # all elements are unique, so it will return the first element
print(statistics.stdev(f1))
print(statistics.variance(f1))


import numpy as np

# print(np.median(f1))
# print(np.mean(f1))
# print(np.std(f1))
# print(np.var(f1))
# print(np.prod(f1))
# print(np.sum(f1))
# print(np.min(f1))
# print(np.max(f1))
# print(np.sort(f1)[::-1])  # sorted in descending order
# print(np.sort(f1))  # sorted in ascending order
# print(np.size(f1))
# print(np.unique(f1))  # all elements are unique, so it will return the same
# print(np.average(f1))
# print(np.cumsum(f1))  # cumulative sum
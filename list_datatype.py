# st1 = 'Neha'
# st2 = 'Fara'
# st3 = 'Sana'
# st4 = 'Uma'
# st5 = 'David'
# st6 = 'jagan'
# st7 = 'Ajay'

# students1 = ['Neha', 'Uma', 'Fara', 'David', 'Sana', 'Jagan', 'Ajay']

# students2 = list(('ravi', 123, True, 56.5, 9+6j, ['A', 1.1, False]))

# students3 = list({34, 56.5, 5-5j, 'Samad', 'Apple@123'})

# students4 = list(['A', 'B', 'C', 'D', 'E', 1, 2, 3, 0.0, 0.1, 0.2, True, False])

# print(f"type of student1 is {type(students1)}")
# print(f"type of student2 is {type(students2)}")
# print(f"type of student3 is {type(students3)}")
# print(f"type of student4 is {type(students4)}")


# l1 = [10, 20, 30, 40]

# print(l1)
# print(type(l1))

# print(l1[0])
# print(l1[1])
# print(l1[2])

# print(l1[-1])
# print(l1[-2])
# print(l1[-3])


# list1 = [12, 24, 36, 48, 60, 72]
# print(list1[2:5:1])
# print(list1[2:5:])
# print(list1[-4:-1:1])

# positive Indexing
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])

# Negative Indexing
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])


#slicing
# print(list1[0:2:1])
# print(list1[2::1])
# print(list1[::2])
# print(list1[::-1])
# print(list1[-1::-2])

##########################################

# BUILT IN METHODS:-

# list2 = ['A', 23, 'Baby', 45.5, True]

# append:- adds element at the end of the list
# list2.append(False)
# print(list2)
# list2.append('Bujji')
# print(list2)

# list2.append(100)
# list2.append(200)
# print(list2)


# extend:- adds new eements at end of the existing elements
# takes multiple arguments

# list2 = ['A', 23, 'Baby', 45.5, True]

# list2.extend([100, 2000, 300])
# print(list2)

# list2.extend(('M', 'N', 12, 5.5, 'Petrol'))
# print(list2)

# list2.extend({0, 0.01, 0.02, 'mala'})
# print(list2)


# insert:- Inserts an item at a specified index.
# list2 = ['A', 23, 'Baby', 45.5, True]

# list2.insert(0, 'apple')
# print(list2)

# list2.insert(3, 'kala')
# print(list2)


####################

# remove:-
# list2 = ['A', 23, 'Baby', 45.5, True]

# list2.remove('Baby')
# print(list2)

# list2.remove(1)
# print(list2)

# list2.remove(1.1)
# print(list2)
# ValueError: list.remove(x): x not in list


# pop

# list3 = [100, 200, 300, 400, 500, 600, 700]
# list3.pop()
# print(list3)

# list3.pop(3)
# print(list3)

# list3.pop(0)
# print(list3)

# list3.pop()
# print(list3)


###################
# clear()
# list3 = [100, 200, 300, 400, 500, 600, 700]
# list3.clear()
# print(list3)


# index
list4 = [11, 22, 33, 44, 55, 66, 77, 22, 11, 99, 88, 22, 11, 66, 22]

# print(list4.index(44))
# print(list4.index(77))


#  count()
# print(list4.count(22))
# print(list4.count(11))
# print(list4.count(77))
# print(list4.count(1000))


# len()
# list5 = ['A', 'a', 1, 2, 3, 4, 5, 6, True, False, [12, 23, 34], 'Mango', 'Nimboo', 56.6]
# print(len(list5))


list6 = [34, 12, 77, 5, 90, 100, 3, 10, 1]
# list6.sort(reverse=True)
# list6.sort()
# print(list6)

# list6.reverse()
# print(list6)

# print(list6[::-1])

# l1 = [1, 2, 3]
# # l2 = [1, 2, 3]

# l2 = l1
# print(l1)
# print(l2)

# print(id(l1))
# print(id(l2))


# j1 = [100, 200, 300]
# j2 = j1.copy()
# print(j1)
# print(j2)

# print(id(j1))
# print(id(j2))


# additional


# ll1 = [1, 2, 3]
# ll2 =  [9, 8, 7]
# print(ll1 + ll1 + ll1 + ll2)


# repetation
# ll1 = [3, 4, 5]
# print(ll1 * 3)
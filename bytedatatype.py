# print(ord('K'))
# print(bin(75))

# print(int('1001011', 2)
# print(chr(75))

#------------------------------------------------

# byte Datatype

    # byte datatype is a represenation ascii numbers
    
    # initialize a byte dattype with byte literal
    
# b1 = b'ABCD'
# print(b1)
# print(b1[0])
# print(b1[1])
# print(b1[2])
# print(b1[3])


# b2 = b"8976"
# print(b2)
# print(b2[0])    # 56
# print(b2[1])
# print(b2[3])


# b3 = b"@#$"
# print(b3[0])

#--------------------------

# b10 = bytes('ABCD','utf-8')
# print(b10)

# print(b10[0])

# print(b10[-1])



# b2= b"ABCD"
# print(b2)


# b_array1 = bytearray("ABCD", 'utf-8')
# print(b_array1)
# print(b_array1[0])



#################

# byte1 = bytes('ABCD', 'utf-8')
# print(byte1)

# byte2 = b'ABCD'
# print(byte2)


b_array1 = bytearray('ABCD', 'utf-8')
print(b_array1)
b_array1.append(69)
print(b_array1)
b_array1.remove(65)
print(b_array1)

print(b_array1.lower()[0])

b_array2 = bytearray('1234', 'utf-8')
print(b_array2.title()[::-1].upper()[2])
print(chr(50))
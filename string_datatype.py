# STRING DATA TYPE:-

# what is string:-
    # if anything is written inside quotes
    # then it is called string data type.
    
# what type of data type is string:-
    # string is an immutable datatype.
        # can not be modified = immutable
    # string does support indexing
    # string is an ordered datatype.
    # string is reffered as str
    
    # '', "", ''' ''', """ """

# review = 'Sir you are not explaining what is """string"""'
# review = "Sir you are not explaining what is 'string'"
# review = '''Sir you are not explaining what is """string"""'''
# review = """Sir you are not explaining what is string"""


# Example of String data type:-

name = "Ayesha"
surname = 'khan'
password = "Shiv@123"
email = "shivkumarmatkawala@gmail.com"

# print(type(name))  #<class 'str'>
# print(type(surname))  #<class 'str'>

x = 5
y = 2.5
z = 3-5j

# print(f"x type is: {type(x)}")
# print(f"y type is: {type(y)}")
# print(f"z type is: {type(z)}")

w = '5'
u = '2.5'
m = '3-5j'
# print(f"w type is: {type(w)}")
# print(f"u type is: {type(u)}")
# print(f"m type is: {type(m)}")


girl = "Sunaina"
# positive Indexing
# print(girl[0])
# print(girl[1])
# print(girl[2])
# print(girl[3])
# print(girl[4])
# print(girl[5])
# print(girl[6])
# print(girl[7])  IndexError: string index out of range

# # Negative Indexing
# print(girl[-1])
# print(girl[-2])
# print(girl[-3])
# print(girl[-4])
# print(girl[-5])
# print(girl[-6])
# print(girl[-7])
# print(girl[-8])  IndexError: string index out of range


# Slicing:-

    # creating pieces
    # start: end: step
    
# password = "Ayan@123"
# print(password[4])

# prinrnt Ayan
# print(password[0:4:4])

# print(password[-8:-4:1])


str100 = '''Yellow is Blue'''
# by using negative indices print 'Yellow'

print(str100[-14:-8:1])

# by using positive indices print'eulB'
print(str100[13:9:-1])

# by using Negative indices print 'si'
# print(str100[-6:-8:-1])

# Bio
# print(str100[-4:-11:-3])
# print(str100[10:3:-3])


#######################################

# In built methods of string in python:-

# str99 = 'APPLE'
# str88 = 'grapes'
# str77 = 'Mango'
# str66 = 'PiNEaPpLE'
# str55 = 'Banana@123'
#     # Case Conversion Methods:-
#     # All case conversion methods work only on alphabetic charecters
# # 1) lower
# print(str99.lower())
# print(str88.lower())
# print(str77.lower())
# print(str66.lower())
# print(str55.lower())

# # 2) upper
# print(str99.upper())
# print(str88.upper())
# print(str77.upper())
# print(str66.upper())
# print(str55.upper())

# # 3) capitalize
# str44 = 'python is an easy 100%'
# str33 = 'Java Is Very HARD 100%'

# print(str44.capitalize())
# print(str33.capitalize())

# # 4) title
# print(str44.title())
# print(str33.title())

# str22 = '1rooma is gone 2custumre'
# print(str22.title())

# # 5) swapcase
# str11 = 'aliAna Dcruze is a BollTwood actREss'
# str00 = 'APPLE grapes'
# str0 = 'Ahemad is 123 year Old'

# print(str00.swapcase())
# print(str0.swapcase())
# print(str11.swapcase())


##################################################

# Search and Replace in built methods of string in python:-

str999 = 'APPLE'
# 1) find
# print(str999.find('A'))
# print(str999.find('P'))
# print(str999.find('Q'))
# print(str999.find('E'))

# 2) rfind
# print(str999.rfind('A'))
# print(str999.rfind('P'))
# print(str999.rfind('E'))

# 3) index
# print(str999.index('A'))
# print(str999.index('P'))
# print(str999.index('E'))
# print(str999.index('M'))   #ValueError: substring not found

# 4) rindex
# print(str999.rindex('A'))
# print(str999.rindex('P'))
# print(str999.rindex('D'))  #ValueError: substring not found

# 5) replace

str888 = 'HELLO'
print(str888.replace('H', 'P'))
print(str888)

print(str888.replace('HELLO', "BYE"))

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
    
password = "Ayan@123"
print(password[4])

# prinrnt Ayan
# print(password[0:4:4])

print(password[-8:-4:1])

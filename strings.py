#strings

message = "bob's world"
message2 = 'bob world'
message3 = """bobs world 
is cool"""
print(message)
print(message2)
print(message3)

#indexing strings
message4 = ' Hello, World '
print(message4[0])
print(message4[-1])

#length, included whitespaces
print(len(message4))

#built in methods
print(message4.strip()) #remove white spaces
print(message4.lower()) #convert all to lower case
print(message4.split(',')) #split a string into a list based on comma
print(message4.upper())

 
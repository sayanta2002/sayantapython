#Creating a multiple line string

string = '''I don't know shit where 
            am I going'''

print(string)

# Indexing allows negative address references to access characters from the back of the String,
# e.g. -1 refers to the last  character,
# -2 refers to the second last character, and so on.
print(len(string))

print("\nThe 1st Character of the string:")
print(string[0])
print("\nThe last Character of the string:")
print(string[46])
print("\nThe second last Character of the string:")
print(string[-1])  #Using negative Index
print("\nThe 3rd last Character of the string:")
print(string[-3])

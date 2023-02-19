# Strings are incommutable but supports Concatenation
# Strings once assigned can't be changed by element

# Python3 program to show that
# string cannot be changed

a = 'Sayanta'
b =  a + " Biswas"

# output is displayed
print(a)

## a[2] = 'E'
#print(a)  # causes error

print(b) #Supported little concatenation
print(id(a)) #tells the identity where the string is stored in memory

#3 ways to create strings

# Python3 program to create
# strings in three different
# ways and concatenate them.

# string with single quotes
a = 'Geeks'

# string with double quotes
b = "for"

# string with triple quotes
c = '''Geeks a portal 
for geeks'''

d = '''He said, "I'm fine."'''

print(a)
print(b)
print(c)
print(d)

# Concatenation of strings created
# using different quotes
print(a + b + c)

print('"Hey so happy to be here"') #Use " ' ' " or ' " " '  Configuration for showing Single or Double Quotes

# use of mix quotes
print('Getting Geeky, "Loving it"')
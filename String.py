name = "Sayanta Biswas" #Strigs can be written using Single or Double quotes
u = len(name)           #len function tells the length of the strings including white spaces
print(u)                #Answer 14 (Including Space ) (Starting from 0 to 13)

print(name[0])          #THat [] (Assignment Operator) is like array in C/C++ . The 0th element is 'S'
print(name[1])
                        #print(u[0]) can't be available because [] does not work on Data Types other than Strings

#Operations on Strings (CHaning Case)
# (Strings are immutable, we can't change them)
#  name[6] = 'C'  run this snippet nad that won't

print(name[5:12])       #this : acts like range like in Excel viz. SUM(A7:Z7)

## UpperCase & LowerCase

print(name.lower())
print(name.upper())
print(name.title())  #Titlesizing means first letter of every word is capital
print(name.isupper())  #.isupper, .islower is OOP s that check whether a string is in uppercase or lowercase (Ans FALSE)
print(name.islower())  #returns in Boolean
print(name.istitle())  #returns in Boolean (Ans TRUE)
print(name[0].isupper()) #Tells the first letter in our string is Uppercase
print(name[1:6].islower())
print(name[5:10].title())
print(name[7].isspace()) #Isspace checks whether it is White Space or not







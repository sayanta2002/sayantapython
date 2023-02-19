fruits = ["Banana", "Apple", "Mango"]
print(fruits)

mylist = [20,30,10,40]
print(mylist)
print(mylist[1]) #Prints the first element like Strings

mylist.reverse()    #It reverses the whole list elements
print(mylist)       #This mylist is not as the one before, code is interpreted line by line
print(mylist[1])

mylist.append("Hey")    #Append function adds an element to the list at the end and increases list size by 1
print (mylist)

Pi = ["You "]
Pi.append("are a ")
Pi.append("Whore")
print(Pi)
Pi.reverse()
print(Pi)

fruits.extend(["Orange" , "Nuts"]) #Use extend to insert one or more elements in the list
print(fruits)                       # attaches elements at the end of the list but the elements gets mixed well

# use insert to plug new elements in a list according to your desired position

fruits.insert(3, "Jackfruit")
print(fruits)

#We can attach strings with strings using extend function

m = [6 , 9 , "Our", "Planet"]
l = ["Earth", "is not", "that Green anymore"]
o = ["well", "for the next century"]

m.extend(l)
print(m)

l.append(o)
print(l)
l.reverse()
print(l)
print(l[2])
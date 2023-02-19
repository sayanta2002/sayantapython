# Python program to demonstrate
# comparison between the three methods

# assign lists
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
list_3 = [1, 2, 3]

a = [2, 3]

# use methods
list_1.append(a)        #They both attach the list but the latter remains unaltered [1,2,3, [2,3] ]
list_2.insert(3, a)
list_3.extend(a)  #Extend increases the list element no  without any separation [1,2,3,2,3]

# display lists
print(list_1)
print(list_2)
print(list_3)
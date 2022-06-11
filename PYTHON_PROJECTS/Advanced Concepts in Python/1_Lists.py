# Lists : ordered, mutable, allows dublicate elements.

myList = ["nipun", "is", "single"]
#print(myList)

myList2 = list() # list() function creats an empty list
#print(myList2)


myList3 = [1, "nipun", True, [1,2], 4.68, "nipun"] # a list can store different data types including list itself, and it allows dublicate elements.
#print(myList3)

# Assecssing an item
name = myList[0]
ststus = myList[2]
#print(f"name :", {name})

myList[-1] # last item in the list
myList3[-2] # second last item in the list and so on...

# Iterating over list

for i in myList3:
    print(i)

# Searching for an item in list

if "nipunnnn" in myList3:
    print(True)
else:
    print(False) 


# Some useful methods for list class -------------------------------------------->

#1 Number of items in the list :

len(myList3)  # counts dublicates as two diffrent items due to different memory allocation

'''
length = len(myList3)
print(length)

'''

#2 Adding items to the end of list :

myList3.append("age")
myList3.append(20)

#print(myList3)

#3 Inserting item to a specific position in list

myList3.insert(2,"sexy") # insterts item at specified index --> insert(index,item)

#print(myList3)

#4 Removing item

myList3.pop() # This will remove the last item from the list and return the item.
last_item = myList3.pop()
#print(last_item)

myList3.remove("sexy") # This will remove the specified item.

myList.clear() # This will remove all the elements and make an empty list

#5 Reversing a list

#myList3.reverse()

#6 Sorting a list

'''
myList3.sort()
print(myList3) ---> This will give an error 
Not supported among instances of differnt data types

'''
myNums = [1, 5, 67, 8, -1, 86, 9, 12, -65, 2000, -866] 
myNums.sort() # sorts list in asscending order
#print(myNums)
                  

                                     # OR

myNums2 = [1, 2, 56, 6, -55, -6333, 200, 233, -66]
sorted_list = sorted(myNums2) # This will store the sorted form of list in the varible, while the orignal list remins unsorted

#print(sorted_list)
#print(myNums2)


#                                       Tips and Tricks

'''Example creating a list with repeated elements'''

rep_list = [0] * 5
rep_list2 = ["sex"] * 5

# Concatinaion of Lists

Con_list = myList3 + myNums2

# List Sclicing

short_list = myList3[0:4] # Returns a subList from -->[start index, end index - 1]
#print(short_list)
a = myList3[:4] # Starts from index 0 till 3.
b = myList3[1:] # Starts from index 1 till end.

# Stepping through index in array

step2 = myList3[0:5:2] # starts from index 0 till index 4, steps thorogh every item with width of 2.
#print(step2)
step_negative = myList3[::-1] # starts from end of list with step size one.
step2_negative = myList3[::-2] # starts from end of list with step size two. 
step_surprise = myList3[1:6:-2] # print and analyze, surprise!!! 
print(myList3)
print(step_surprise)

# Copying methods

#1 ------------------>
Fruits = ["apple", "banana", "orange"]
'''
Vegetables = Fruits

This is not a good technique to copy the lists, because it copies the memory address of one list to the other.
Althoough, our list would be copied into another list, any change made into the assigned list will also take place in our origional list.
This is because we are copying the memory address ofone list to the other and not the actual items.

For example:

Vegetables.append("carrot")

observe :- 
print(Vegetables)
print(Fruits)

'''
#2 ------------------->

Vegetables = Fruits.copy()
Vegetables.append("Tomato")
#print(Vegetables)
#print(Fruits)


#3 ------------------->

Vegetables = list(Fruits)
Vegetables.append("Tomato")
#print(Vegetables)
#print(Fruits)

#4 -------------------->

Vegetables = Fruits[:] 
Vegetables.append("Tomato")
print(Vegetables)
print(Fruits)


# List Comprehension (Advanced Technique)
# --> This is a fast way to create a new list from an existing list, with only one line.

comp_list = [1, 2, 3, 4, 5, 6]
same_list = [i for i in comp_list]
sq_list = [i * i for i in comp_list]
cube_list = [i*i*i for i in comp_list]

# Using i as a vrible we can itrerate through list

# General Syntax -------------------> oldList = newList[ {expression using a variable (say i)} for {i} in {oldList} ]

print(comp_list)
print(same_list)
print(sq_list)
print(cube_list)


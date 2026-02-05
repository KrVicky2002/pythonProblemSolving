# Pyhton program that takes a list of numbers , removes all duplicate elements and returns new list. 
#steps
# create a new empty list
# go through each element of the list one by one by one by using loop (for).
# add an element to the new list only if already not present in it.

numbers = [1,2,3,2,4,4,5,6,3]

newList = []

for ele in numbers:
    if(ele not in newList):
        newList.append(ele)


print(newList)
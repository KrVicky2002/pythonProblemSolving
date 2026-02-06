# Python progrma that takes a list of integers, find and print second largest number in the list.

list = [1,2,4,6,3,5,2,7,9,8]
largest = list[0]
secondLargest = 0

for num in list:
    if num > largest:
        secondLargest = largest
        largest = num
    elif num < largest and num > secondLargest:
        secondLargest = num
        
print(largest)
print(secondLargest)

#Program that checks how many even and odd numbers are present in list

list = [1,2,3,4,4,5,6,7,8,9,6,2,2,4,11,1234]

even = 0
odd = 0

for ele in list:
    if ele % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Total even numbers in list are:{even}")
print(f"Total odd numbers in list are:{odd}")


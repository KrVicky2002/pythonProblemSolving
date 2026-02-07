# Program that checks values how many time repeated in list.

list = [1,2,3,4,5,2,5,6,2,4,7]
# newList = []

# for ele in list:
#     if ele not in newList:
#         newList.append(ele)

# for item in newList:
#     element = list.count(item)
#     print(f"{item} repeated {element} times.")


# more optimize way using dictionary

count_dict = {}

for ele in list:
    if ele in count_dict:
        count_dict[ele] += 1
    else:
        count_dict[ele] = 1

for key , value in count_dict.items():
    print(f"{key} repeated {value} times")
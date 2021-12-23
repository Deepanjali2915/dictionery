# Write a program to print the top 3 highest values of a given dictionary.
# my_dict = {
# 'a':50,
# 'b':58,
# 'c': 56,
# 'd':40,
# 'e':100,
# 'f':20
# }
# expect result:-['e','b','c']


my_dict = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
# max=0
max1=[]
for i in range(3):
    max=0
    for j in my_dict:
        if my_dict[j]>max:
            max=my_dict[j]  
            h=j          #why
    max1.append(h)
    my_dict.pop(h)
print((max1))






















# for i in my_dict:
#     if my_dict[i]>max:
#         max = my_dict[i]
#         s=i
# max1.append(s)
# second_max = 0
# for i in my_dict:
#     if my_dict[i]> second_max:
#         if my_dict[i]!= max:
#             second_max=my_dict[i]
#             s=i
# max1.append(s)
# third_max = 0
# for i in my_dict:
#     if my_dict[i]> third_max:
#         if my_dict[i]!= max and my_dict[i]!=second_max:
#             third_max=my_dict[i]
#             s=i
# max1.append(s)
# print(max1)


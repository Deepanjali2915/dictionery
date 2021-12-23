# question11















# QUESTION 13
# # Q13.Write a Python program to sum all the items in a dictionary.
# dict = {'a': 100, 'b':200, 'c':300}     
# sum=0
# for i in dict:
#     # print(dict[i])
#     sum=sum+dict[i]
# print(sum)

# question14
# Q14.Write a Python program to multiply all the items in a dictionary.

# dict = {'a': 9, 'b':2, 'c':3}
# multiply=1
# for i in dict:
#     multiply=multiply*dict[i]
# print(multiply)



# question15
# # Q15.Write a Python program to remove a key from a dictionary.
# dict = {'a': 9, 'b':2, 'c':3}
# for i in dict:
#     dict.pop("c")
#     print(dict)



# question 20
# Q20.Write a Python program to check a dictionary is empty or not.
# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# dict1 = {'a': 100, 'b': 200, 'c':300}
# dict2 = {'a': 300, 'b': 200, 'd':400}
# for i in dict1:
#     if i in dict2:
#         dict2[i]=dict1[i]+dict2[i]
#     else:
#         dict2[i]=dict1[i]
# print(dict2)            





# Q25. Write a Python program to create a dictionary from a string./
# Note: Track the count of the letters from the string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# name=input("Enter the name: ")
# snippt={}
# for i in name:
#     if i in snippt:
#         snippt[i]+=1
#     else:
#         snippt[i]=1
# print(snippt)            







# a=[{"math":5,"science":7},{"math":4,"science":8},{"math":2,"science":6}]
# sub=str(input("enter the subject: "))
# add=0
# i = 0
# while i < len(a):
#     for j in a[i]:
#         if j == sub:
#             add+=a[i][j]
#         i+=1
# print(add)



# for i in range(len(a)):
#     for j in a[i]:
#         if j == sub:
#             add+=a[i][j]
# print(add)      


# a=[1,2,3,6,5,4,2,7,8,1,2,3,4,5,1,2,3,4]
# x={}
# for i in a:
#     s=a.count(i)
#     d=s//2
#     x.update({i:d})
# print(x)    

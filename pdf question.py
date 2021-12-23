# # Q19.
# # # Write a Python program to remove duplicates from Dictionary.
# student_data = {'id1':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']},
#                 'id2':{'name': ['David'],'class': ['V'],'subject_integration': ['english, math, science']},
#                 'id3':{'name': ['Sara'],'class': ['V'],'subject_integration': ['english, math, science']},
#                 'id4':{'name': ['Surya'],'class': ['V'],'subject_integration': ['english, math, science']},}

# result = {}

# for key,value in student_data.items():
#     if value not in result.values():
#         result[key] = value

# print(result)



# Q21.Write a Python program to print all unique values in a dictionary.
# SampleData =[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}]
# {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# result={}
# for key,value in range(len(SampleData)):
#     if value not in result.values():
#         result[key]=value
# print(result)        
# a=[]
# for i in SampleData:
#     for j in i.values():
#         a.(j)
# print([a])















# Q22. Write a Python program to create and display all combinations of letters, selecting each
# letter from abc import ABC
# from a different key in a dictionary. Go to the editor
# Sampledata={'1':['a','b'], '2':['c','d']}
# Expected /Output:

# ac
# ad
# bc
# # bd
#
# for i in Sampledata["1"]:
#     for j in Sampledata["2"]:
#         print(i+j)
        # print(Sampledata[i][j])
# 


# question24
# Write a Python program to combine values in python list of dictionaries.


# Sampledata=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1','amount': 750}]
# f=[]
# u=[]
# for i in Sampledata:
#     if i["item"] not in u:
#         u.append(i["item"])
#         f.append({"item":i["item"], 'amount': 0})
# # print(f)
# for i in f:
#     for k in Sampledata:
#         if i["item"]==k["item"]:
#             i["amount"]+=k["amount"]
# print(f)

# f=[]
# # n={}
# for i in Sampledata:
#     # n={}
#     if n["item"]==i["item"]:
#         n["amount"]+=i["amount"]
#     else:
#         n["item"]=i["item"]
#         n["amount"]=i["amount"]
#         f.append(n)

# # Expected Output: Counter({'item1': 1150, 'item2': 300})
# add=1
# for i in range(len(Sampledata)): 
#     for j in Sampledata[i]:
#         if i in Sampledata:
#             add+=Sampledata[i][j] 
# print(add)                 


# combine={}
# add=0
# for i in Sampledata:
#     for j in i:
#         if i["item"] not in Sampledata:
#             add+=Sampledata[i][j]     
#             combine[i["item"]]=i["amount"]
#             combine.update(Sampledata)
# print(combine)        

# question26
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# C1 C2 C3
# 1,5,9
# 2,6,10
# 3,7,11


# count=[0,0,0]
# for key,value in my_dict.items():
    # for i in my_dict[key]:
        # print(i)
        # count+=1
        # for i in range(len(my_dict[key])):
        #   /  count[i]+=my_dict[i]
            # count+=1
# print(count)            


# # Q27.Write a Python program to count the values associated with key in a dictionary.
# student = [{'id': 1, 'success': True, 'name': 'Lary'},
# {'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]
# # Sample input if key is id: then 6
# sum=0
# for i in student:
#     sum+=i["id"]
# print(sum)



# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}
# num_list = [1, 2, 3, 4]
# new_dict = new= {}
# for name in num_list:
#     new[name] = {}
#     new = new[name]
# print(new_dict)






# Q32.Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Output:
# key value count
# 1   10      1
# 2   20      2
# 3   30      3
# 4   40      4
# 5   50      5
# 6   60      6
# count=0
# for i in dict_num:
#     count=i
#     print(i,dict_num[i],count)
    # print(dict_num(i))




# Q35. Write a Python program to count the number of items in a dictionary value that is a list.
# dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# # # Sample output: 5
# count=0
# for i in dict:
#     # for j in dict[i]:
#         # count+=1
#         count+=len(dict[i])
# print(count)



# # Q39.Write a Python program to filter a dictionary based on values.
# # Original Dictionary:
# greater={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# # # Marks greater than 170:
# # # {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
# a={}
# for (key,value) in greater.items():
#     if value>=170:
#         a={key:value}
#         print({a})


# a= new={}
# n=int(input("enter the number: "))
# for i in range(n):
#     k=input("enter the key: ")
#     l=input("enter the value: ")
#     a.update({k:l})
#     m=int(input("enter the number"))
#     l={}
#     for j in range(m):
#         c=input("enter the key: ")
#         d=input("enter the value: ")
#         l.update({c:d})
# print(new)    








d = {}

size = int(input("Enter the size of nested dictionary: "))
for i in range(size):
    
    dict_name = input("Enter the name of child dictionary: ")
    d[dict_name] = {}
    size1=int(input("enter the size"))
    for j in range(size1):
        Name = input("Enter key: ")
        Age = input("Enter value: ")
        # d[dict_name][Name] = {}
        # d[dict_name][Age] = {}
        dict_name[j]=Name
# print(d)    /
print(d[dict_name])
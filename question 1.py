# Write a program such that the below given dictionaries are into a single dictionary
# #  and add the values having same key.


dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# # print(dic1+dic2+dic3)
# dic1.update(dic2)
# dic1.update(dic3)
# dic1.values()
# print(dic1)


# for i,j in dic2,dic3:
#     if i in dic1 or j in dic1:
#         dic1[i]=dic2[i]+ dic3[i]+dic1[i]
#     else:
#         dic1[i]=dic2[i]
#         dic1[i]=dic3[i]

# print(dic1)            
for i in dic1:
    if i in dic2:
        dic2.append(dic1)
print(dic2)
# Write a program to sort a dictionary in ascending
#  or descending according to its values .

# {'bijender':45,'deepak':60,'param':20,';'anjili':30,'roshini':50}




# Number={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
# NumList={}
# name={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
# short={}

# for i in name:
#     for j in i:
#         if name[j]==i:
#             # type(name[i])==int 
#             print(name[i])
#             c=name[i]
#             name[i]=name[i+1]
#             name[i+1]=c
# print(name)

# for i in name:
#     s=name[i]
#     for j in name:
#         a=name[j]
#         if a>s:                     
#             short[j]=a
            # short[i]=short[j]
            # short[j]=a
# print(short)            
# # print(s)
# print(a)
# print(short)



# for i in range (Number):
#     for j in range(i + 1, Number):
#         if(NumList[i] > NumList[j]):
#             temp = NumList[i]
#             NumList[i] = NumList[j]
#             NumList[j] = temp

# print("Element After Sorting List in Ascending Order is : ", NumList)



# milk, student, dist pan,home,clean, bad free,damage bed, 

name={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}
short={}
val=[]
for j in name:
    val.append(name[j])
for i in range(len(val)):
        for k in range(len(val)-1):
            if val[i]>val[k]:
                temp=val[i]
                val[i]=val[k]
                val[k]=temp
for i in val:
    for k in name:
        if name[k]==i:
            short[k]=i
print(short)


        # vallist.append(temp)
            # if name[i]>name[k]:
            #     short[i]=name[i]
# print(short)
# for i in name:
#     s=name[i]
#     for j in name:
#         a=name[j]
#         if a>s:                     

# print(short)      
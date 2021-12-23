# my_dict = {
# 'data1':100,
# 'data2': -54,
# 'data3': 247
# }
# sum=0
# for i in my_dict:
#     sum+=my_dict[i]
# print(sum)    






num=int(input("enter the number: "))
total=num/360*100
if num<=total:
    print(total,"no")
else:
    print(total,"yes")    
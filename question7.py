# Take a list having dictionary elements as shown below
#  (Sample Data) and then store all the unique values into a list and print.
# [{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
# output=[2', '7', '9', '5', '1']



dict=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
list =[] # create empty list
for i in dict:
    for j in i.values():
        if j not in list: 
            list.append(j)
         # else:
        #     pass
print (list)
    




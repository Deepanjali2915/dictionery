# Write a program to print the top 3 highest values of a given dictionary.
my_dict = {
'a':50,
'b':58,
'c':56,
'd':40,
'e':100,
'f':20
}

# max=0
max1=[]
for i in range(3):
    max=0
    for j in my_dict:
        if my_dict[j]>max:
            max=my_dict[j]
            c=j
        # max1.append(c)
    max1.append(my_dict[c])
    my_dict.pop(c)              #why
            # max1.append(max)
            # max1.my_dict
print(max1)

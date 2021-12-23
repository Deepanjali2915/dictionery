# row=int(input("enter the row: "))
# i=0
# while i<=row:
#     j=1
#     while j<=row-i:
#         print(j,end="")
#         j+=1
#     i+=1
#     print()    



 
# number = int(input("Enter the integer number: "))  
# i=0
# while number>0:
#     i=(i*10)+number%10
#     number=number//10
# print(i)    
# k=i//10
# print(k*10)



# n=int(input("enter the number: "))
# i=1
# count=0
# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:      
#     print(n,"it is a prime number: ")
# else:
#     print(n,"not a prime")      



# i=int(input("Enter the number:"))
# if i%1==0 and i%i==0 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i%9!=0:
#     print("it is a prime no.:")
# else:
#     print("not a prime number.:")    


# a={1:10,2:20,3:30}
# b={4:40,5:50,6:60}
# c={7:70,8:80,9:90}
# a.update(b)
# a.update(c)
# print(a)


a={"a":100,"b":200,"c":300}
b={"a":300,"b":200,"d":400}
# c={}
# for i in a.values():
#     for j in b.values():
#         c.update({a[i]+b[j]})
# print(c)        


for i in a:
    a[i]
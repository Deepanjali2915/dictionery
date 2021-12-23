# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were
#  the letters are the keys and their frequencies are the values.

{'M':1,'I':4,'S':4,'P':2}

a=input("Entert the word")
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1    
print(b)
print((b))
print(str(b))



n=input()
x=input()
c=0 
for i in range(1,len(x)):
    if x[i]==x[i-1]:
        c+=1
print(c) 

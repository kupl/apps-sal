# cook your dish here
def f(lst1,lst2):
    dict1={}.fromkeys(lst1,0)
    for key in lst1:
        dict1[key]+=1
    s=max(dict1.values())
    for i in dict1:
        if(dict1[i]==s):
            key=i
            break
    lst3=[]    
    for i,j in zip(lst1,lst2):
        if(i!=key):
            lst3.append(j)
    dict2={}.fromkeys(lst3,0)
    for key in lst3:
        dict2[key]+=1
    s1=max(dict2.values())
    return s+s1
r,c,n=list(map(int,input().split()))
lst1=[]
lst2=[]
for i in range(n):
    r,c=list(map(int,input().split()))
    lst1.append(r)
    lst2.append(c)
print(max(f(lst1,lst2),f(lst2,lst1)))
        


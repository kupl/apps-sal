# cook your dish here
def sm (b):
    v=0;
    v=b%10
    c=0
    while (b!=0):
        c=b%10
        b=b//10
    return(v+c)
n=int(input())
a=[]
for i in range (0,n):
    no=int(input())
    a.append(no)
for i in range (0,n):
    print(sm(a[i]))

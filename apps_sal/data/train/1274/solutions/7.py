# cook your dish here
t=int(input(""))
while(t!=0):
    s=''
    k=int(input(""))
    #print(k)
    for i in range(k):
        for j in range(k):
            s=s+str(j+1)+str(i+1)
        print(s)
        s=''
    t-=1

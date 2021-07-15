# cook your dish here
for _ in range(int(input())):
    n=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    p=int(input())
    c=0
    while p>=1:
        m=[]
        for q in n:
            if(p>=q):
                m.append(p-q)
        p=min(m)
        c+=1
    print(c)

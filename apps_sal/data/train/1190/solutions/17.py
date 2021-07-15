# cook your dish here
t = int(input())

for i in range(t):
    a = int(input())
    l=[1,2,4,8,16,32,64,128,256,512,1024,2048]
    z=0
    while a>=1:
        m=[]
        for i in l:
            if a>=i:
                m.append(a-i)
           
        a= min(m)
        
        z+=1
    print(z)
    


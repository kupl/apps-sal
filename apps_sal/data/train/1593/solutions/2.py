n=int(input())
for i in range(n):
    a=int(input())
    note=0
    while a!=0:
        if a>=100:
            a-=100
        elif a>=50:
            a-=50
        elif a>=10:
            a-=10 
        elif a>=5:
            a-=5 
        elif a>=2:
            a-=2
        else:
            a-=1 
        note+=1 
    print(note)
        


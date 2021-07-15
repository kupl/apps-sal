import math
t=int(input())
#t=1
for i in range(t):
    #n=int(input())
    s,sg,fg,d,t=map(int,input().split())
    #l=list(map(int,input().split()))
    #s=input()
    tot=(d*50*3.6)/t
    final=s+tot
    a=abs(final-sg)
    b=abs(final-fg)
    #print(tot,final,a,b)
    if(a<b):
        print("SEBI")
    elif(b<a):
        print("FATHER")
    else:
        print("DRAW")


    

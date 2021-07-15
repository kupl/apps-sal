t=int(input())
for hh in range(0,t):
    n,k=[int(x) for x in input().split()]
    # 2 3
    m=1000000007
    pos=n
    if(n==0):
        rem=k-1
        cur=(rem*(rem+1))%m
        print(cur)
    elif(k==1):
        prev=(pos*(pos-1))%m
        curr=(prev+pos)%m
        print(curr)
    else:
        # if(k%2==1):
        #     p=k//2
        #     # p=1
        #     inipos=pos
        #     pos=pos+p-1
        #     prev=pos*(pos+1)
        #     print(prev,pos)
        #     curr=prev+inipos
        #     print(curr)
        # else:
        #     p=k//2 -1 
        #     inipos=pos
        #     # pos=4 k = 6 p=2
        #     pos=pos+p-1
        #     prev=pos*(pos+1)
        #     now=inipos+p
        #     rem=now-inipos
        #     print(prev,now,pos,p,rem)
        #     curr=prev+now+rem
        #     print(curr)
        if(k%2==1):
            k-=1
            p=k//2
            # p=1
            ans=2*pos
            inipos=pos
            # pos=4 k = 6 p=2
            pos=(pos+p-1)%m
            prev=(pos*(pos+1))%m
            now=(inipos+p)%m
            rem=(now-inipos+m)%m
            # print(prev,now,pos,p,rem)
            curr=(prev+now+rem)%m
            print(curr)
        else:
            k-=1
            p=k//2
            # p=1
            # pos =4 k =6 k=5 p=2
            inipos=pos
            pos=(pos+p)%m
            prev=(pos*(pos+1))%m
            # print(prev,pos)
            curr=(prev+inipos)%m
            print(curr)

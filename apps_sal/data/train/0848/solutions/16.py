try:
    t=int(input())
    for s in range(0,t):
        n=int(input())
        l=list(map(int,input().strip().split()))
        a=len(l)
        i=0
        max=-999999
        while(i<a):
            sum=0
            if(i==(a-1)):
                sum=l[i]+l[0]+l[1]
            elif(i==(a-2)):
                sum=l[i]+l[i+1]+l[0]
            else:
                sum=l[i]+l[i+1]+l[i+2]
            if(sum>max):
                max=sum
            i=i+1
        print(max)
except:
    pass


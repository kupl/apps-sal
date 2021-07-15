# cook your dish here
t=int(input())
while(t): 
    l=list(map(int,input().split()))
    count=0
    div=0
    evenSum=0
    for i in range(0,len(l)-1):
        if(l[i]>30):
            count+=1 
        if(l[i]%2==0):
            evenSum+=l[i]*(i+1)
            div+=i+1
    average=evenSum/div 
    print('%d %.2f'%(count,average))
    t-=1

# cook your dish here
test=int(input())
while(test!=0):
 n,k,d=list(map(int,input().split()))
 li=list(map(int,input().split()))
 days=sum(li)//k 
 print(min(days,d))
 test=test-1 


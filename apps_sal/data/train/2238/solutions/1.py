for i in range(int(input())):
 l,r=list(map(int,input().split()))
 while(l|(l+1)<=r): l|=l+1
 print(l)


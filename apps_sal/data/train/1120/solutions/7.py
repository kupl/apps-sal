# cook your dish here
for t in range(int(input())):
 #n=int(input())
 r,c=map(int,input().split())
 x,y=map(int,input().split())
 #arr=list(map(int,input().split()))
 print(max(abs(c-y-1),y)+max(abs(r-x-1),x))

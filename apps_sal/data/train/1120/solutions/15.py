# cook your dish here
#872
for _ in range(int(input())):
 n,m=[int(x)for x in input().split()]
 x,y=[int(x)for x in input().split()]
 ss=max(x+y,x+m-y-1,y+n-x-1,m+n-x-y-2)
 print(ss)

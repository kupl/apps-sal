# cook your dish here
t=int(input())
for i in range(t):
     n=int(input())
     s=0
     for i in range(1,n+1):
          s+=(i**3)
          # print(i,s)
     s*=2
     s-=n**3
     print(s)


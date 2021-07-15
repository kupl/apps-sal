t=int(input())
for i in range(t):
     x,n=[int(g) for g in input().split()]
     sal=0
     day=x
     while day<n:
          sal=sal+day
          day+=x
     print(sal)


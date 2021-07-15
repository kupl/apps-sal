# cook your dish here
t=int(input())
while t!=0:
    x,y,z=[int(k) for k in input().split()]
    if x+y+z==180:
        print("YES")
    else:
        print("NO")
    t-=1

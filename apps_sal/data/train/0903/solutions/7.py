# cook your dish here
t=int(input())
for _ in range(t):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    ans=(y1*x2 + y2*x1)/(y1+y2)
    print("{0:.2f}".format(ans))

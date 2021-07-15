# cook your dish here
t = int(input())
while t>0:
    x,y = map(int, input().split())
    sum1 = 0
    for i in range(y, x+1, y):
        sum1+=int(str(i)[-1])
    print(sum1)
    t-=1

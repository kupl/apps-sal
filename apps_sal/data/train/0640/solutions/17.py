import math
for _ in range(int(input())):
    x,y=[int(x) for x in input().split()]
    if x==y:
        print(0)
        continue
    else:
        p=math.gcd(x,y)
        xx=(x*y)//p
        # print(xx)
        print(int((xx//x)+(xx/y)-2))
        


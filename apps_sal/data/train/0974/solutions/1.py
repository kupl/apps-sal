# cook your dish here
# COPIED FROM SDG
import math
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    ans1=abs(a-b)
    if ans1==0:
        print("YES")
    else:
        ans2=abs(c-d)
        if ans2==0:
            print("NO")
        else:
            ans=ans1/ans2
            if math.floor(ans)==math.ceil(ans):
                print("YES")
            else:
                print("NO")

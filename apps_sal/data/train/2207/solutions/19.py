n = int(input())
q = 0
e = 0
w = 0
r = 0
for i in range(n):
    t, x, y = map(int, input().split())
    if(t == 1):
        q+=x
        w+=10
    else:
        e+=x
        r+=10
if(q < w//2):
    print("DEAD")
else:
    print("LIVE")
if(e < r//2):
    print("DEAD")
else:
    print("LIVE")

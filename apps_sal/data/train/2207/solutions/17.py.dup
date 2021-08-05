n = int(input())
res1success = 0
res1fail = 0
res2success = 0
res2fail = 0
for i in range(n):
    s, x, y = list(map(int, input().split()))
    if s == 1:
        res1success += x
        res1fail += y
    else:
        res2success += x
        res2fail += y

if res1success >= res1fail:
    print("LIVE")
else:
    print("DEAD")

if res2success >= res2fail:
    print("LIVE")
else:
    print("DEAD")

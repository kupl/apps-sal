s1 = 0
s2 = 0
for _ in range(int(input())):
    l = []
    l = list(map(int, input().split()))
    s = int(l[0])
    n = int(l[1])
    k = int(l[2])
    r = int(l[3])
    if(r != 1):
        s -= (k * ((r**n) - 1)) // (r - 1)
    else:
        s -= k * n
    if(s >= 0):
        print("POSSIBLE", s)
    else:
        print("IMPOSSIBLE", abs(s))
    if(s > 0):
        s1 += s
    else:
        s2 += abs(s)
if(s1 >= s2):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

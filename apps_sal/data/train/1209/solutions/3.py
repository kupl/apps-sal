t = int(input())
for you in range(t):
    l = input().split()
    v1 = int(l[0])
    t1 = int(l[1])
    v2 = int(l[2])
    t2 = int(l[3])
    v3 = int(l[4])
    t3 = int(l[5])
    if(t2 > t1):
        t1, t2 = t2, t1
        v1, v2 = v2, v1
    if(t3 - t2 < 0):
        print("NO")
        continue
    if(v3 * t3 - v3 * t2 > v1 * (t1 - t2)):
        print("NO")
        continue
    if(t3 - t2 > t1 - t2):
        print("NO")
        continue
    if((v3 - v2) * (t1 - t2) > v3 * (t3 - t2)):
        print("NO")
        continue
    print("YES")

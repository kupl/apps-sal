t = int(input())
while t:
    v1, t1, v2, t2, v3, t3 = list(map(int, input().strip().split(' ')))
    if t3 <= max(t1, t2) and t3 >= min(t1, t2):
        if v3 < (v1 + v2):
            if t1 == t2 == t3:
                print("YES")
            elif t3 == t1 and t1 != t2:
                if v3 <= v1:
                    print("YES")
                else:
                    print("NO")
            elif t3 == t2 and t1 != t2:
                if v3 <= v2:
                    print("YES")
                else:
                    print("NO")
            elif t1 == t2 and t2 != t3:
                print("NO")
            elif v2 >= (v3 * (t3 - t1)) / (t2 - t1) and v1 >= (v3 * (t2 - t3)) / (t2 - t1):
                print("YES")
            else:
                print("NO")
        elif v3 == (v1 + v2):
            if v3 * t3 == (v1 * t1 + v2 * t2):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
    t -= 1

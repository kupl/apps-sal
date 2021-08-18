import math
for t in range(int(input())):
    d = int(input())
    s = input()
    k = math.ceil(75 * d / 100)
    p = s.count("P")
    if k <= p:
        print(0)
    else:
        req = k - p
        c = 0
        for i in range(2, d - 2):
            if s[i] == "A":
                if "P" in s[i - 2:i + 1] and "P" in s[i + 1:i + 3]:
                    c += 1
            if c == req:
                print(c)
                break
        else:
            print(-1)

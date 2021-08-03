import math
t = int(input())
for _ in range(t):
    f = 0
    s = input()
    r = s.lower()
    if "berhampore" in r and "serampore" in r:
        f = 1
        print("Both")
    if "berhampore" in r:
        if f == 0:
            f = 1
            print("GCETTB")
    if "serampore" in r:
        if f == 0:
            f = 1
            print("GCETTS")
    if f == 0:
        print("Others")

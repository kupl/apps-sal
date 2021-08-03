t = int(input())
for nt in range(t):
    s = input()
    l, r, u, d = 0, 0, 0, 0
    for i in s:
        if i == "L":
            l += 1
        elif i == "R":
            r += 1
        elif i == "U":
            u += 1
        else:
            d += 1
    if l != 0 and r != 0 and u != 0 and d != 0:
        if l == r and u == d:
            print(len(s))
            for i in range(l):
                print("L", end="")
            for i in range(u):
                print("U", end="")
            for i in range(l):
                print("R", end="")
            for i in range(d):
                print("D", end="")
        else:
            if l == r:
                print(len(s) - abs(u - d))
                for i in range(l):
                    print("L", end="")
                for i in range(min(d, u)):
                    print("U", end="")
                for i in range(l):
                    print("R", end="")
                for i in range(min(d, u)):
                    print("D", end="")
            else:
                print(len(s) - (abs(u - d) + abs(l - r)))
                for i in range(min(l, r)):
                    print("L", end="")
                for i in range(min(d, u)):
                    print("U", end="")
                for i in range(min(l, r)):
                    print("R", end="")
                for i in range(min(d, u)):
                    print("D", end="")
        print()
    else:
        if (l == 0 or r == 0) and (u != 0 and d != 0):
            print(2)
            print("UD")
        elif (u == 0 or d == 0) and (l != 0 and r != 0):
            print(2)
            print("LR")
        else:
            print(0)
            print()

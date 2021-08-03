q = int(input())
for test in range(0, q):
    s = str(input())
    L = s.count('L')
    R = s.count('R')
    U = s.count('U')
    D = s.count('D')
    x = min(L, R)
    y = min(U, D)
    if x == 0 and y == 0:
        print("0")
    elif x == 0:
        print("2")
        print("UD")
    elif y == 0:
        print("2")
        print("LR")
    else:
        print((str(2 * x + 2 * y)))
        ans = ""
        for i in range(0, y):
            ans += "U"
        for i in range(0, x):
            ans += "R"
        for i in range(0, y):
            ans += "D"
        for i in range(0, x):
            ans += "L"
        print(ans)

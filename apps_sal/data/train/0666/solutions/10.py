try:
    for i in range(int(input())):
        n = int(input())
        s = 0
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                s += 1
                print(s, end="")
            print("\r")
except Exception:
    pass

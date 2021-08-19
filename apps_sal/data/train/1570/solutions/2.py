def Solve5():
    n = int(input())
    s = n * (n + 1) * (2 * n + 1) // 6
    print(s)


for _ in range(int(input())):
    Solve5()

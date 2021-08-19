for _ in range(int(input())):
    a = []
    n = int(input())
    for i in range(n):
        s = input()
        a.append(s)
    print(n * (n + 1) // 2)

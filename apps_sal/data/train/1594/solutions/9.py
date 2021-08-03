def fact(n):
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n) + 1):
            factorial = factorial * i
    return factorial


t = int(input())
for i in range(t):
    n = int(input())
    s = []
    for j in range(n):
        s.append(input())
    print(int((fact(n) / (fact(n - 2))) / 2) + n)

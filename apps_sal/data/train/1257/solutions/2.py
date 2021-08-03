T = eval(input())
T = int(T)
while T:
    n = eval(input())
    total = 1
    n = int(n)
    for i in range(1, n + 1):
        total = total * i
    print(total)
    T = T - 1

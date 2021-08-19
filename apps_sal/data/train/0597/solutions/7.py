for _ in range(int(input())):
    n = int(input())
    x = []
    p = []
    for j in range(n):
        (a, b) = list(map(int, input().split()))
        x.append(a)
        p.append(b)
    differences = []
    for u in range(n - 1, 1, -1):
        differences.append(x[u] - x[u - 2])
    differences.append(x[-1] - x[-2])
    differences.append(x[1] - x[0])
    differences.sort()
    p.sort()
    answer = 0
    while len(differences) > 0:
        answer = answer + p.pop() * differences.pop()
    print(answer)

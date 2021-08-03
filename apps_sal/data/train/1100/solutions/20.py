def diff(x, y):
    ans = []

    for i in range(3):
        if x[i] > y[i]:
            return -1
        if x[i] != y[i]:
            ans.append(abs(x[i] - y[i]))
    return sum(ans)


for _ in range(int(input())):
    q = list(map(int, input().strip().split(" ")))
    a = list(map(int, input().strip().split(" ")))
    print(diff(q, a))

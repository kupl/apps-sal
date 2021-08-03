test = int(input())
for _ in range(test):
    n = int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    s = 0
    for i in range(n):
        if s >= ls[i]:
            s = s + 1
        else:
            break
    print(s)

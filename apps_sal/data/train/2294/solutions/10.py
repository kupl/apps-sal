n = int(input())
lis = []
a, b = [], []
for i in range(n):
    X, Y = map(int, input().split())
    lis.append([min(X, Y), max(X, Y)])
    a.append(min(X, Y))
    b.append(max(X, Y))
lis.sort()
answer = (max(a) - min(a)) * (max(b) - min(b))
a_max, b_min = max(a), min(b)
current = float("inf")
for i in range(n):
    if lis[i][0] > b_min:
        current = min(current, a_max - b_min)
        break
    current = min(current, a_max - lis[i][0])
    a_max = max(a_max, lis[i][1])
print(min(answer, current * (max(b) - min(a))))

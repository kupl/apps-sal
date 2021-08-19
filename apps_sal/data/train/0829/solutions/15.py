t = int(input())
s = list(map(int, input().split()))
revenue = 0
for i in range(t - 1):
    for j in range(i + 1, t):
        add = s[i] - s[j]
        if add > 0:
            revenue += add
        else:
            revenue -= add
print(revenue)

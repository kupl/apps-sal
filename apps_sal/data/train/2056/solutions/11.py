n = int(input())
a = input()
b = input()
i = 0
cost = 0
while i < n:
    if a[i] == b[i]:
        i += 1
    elif a[i] != b[i] and i + 1 < n and (a[i + 1] != b[i + 1]) and (a[i] != a[i + 1]):
        i += 2
        cost += 1
    else:
        i += 1
        cost += 1
print(cost)

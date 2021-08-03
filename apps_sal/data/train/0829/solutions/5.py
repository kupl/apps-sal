n = int(input())
a = list(map(int, input().strip().split()))
s = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        s += abs(a[j] - a[i])
print(s)

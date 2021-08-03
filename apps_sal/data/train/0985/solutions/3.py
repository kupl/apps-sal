arr = []
n = int(input())
d = [1] * n
for j in range(n):
    x = int(input())
    for i in range(len(arr)):
        if x % arr[i] == 0:
            d[j] = max(d[j], (d[i] + 1))
    arr.append(x)
print(max(d))

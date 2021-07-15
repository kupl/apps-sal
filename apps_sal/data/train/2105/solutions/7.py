last = 1
n = int(input())
arr = [1]*(n + 2)
for i in range(2, n + 2):
    if arr[i] != 1:
        continue
    for j in range(2*i, n + 2, i):
        if arr[j] == arr[i]:
            arr[j] += 1
            last = max(last, arr[j])
print(last)
print(" ".join(map(str, arr[2:])))


n = int(input())
arr = [int(i) for i in input().split()]
q = int(input())
for _ in range(q):
    sub = 0
    k = int(input())
    for i in range(n):
        for j in range(i + 1, n + 1):
            if min(arr[i:j]) == k:
                sub = sub + 1
    print(sub)

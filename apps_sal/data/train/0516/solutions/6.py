# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    x, suffix = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i] > arr[j]:
                x += 1
            if j > i:
                if arr[i] > arr[j]:
                    suffix += 1
    print(x * ((k * (k - 1)) // 2) + suffix * k)

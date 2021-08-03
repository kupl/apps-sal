for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    i = 0
    while i < n and a[i] == 0:
        i += 1
    j = n - 1
    while a[j] == 0 and j > i:
        j -= 1
    print(j - i + 1 if j - i + 1 != 0 else 1)

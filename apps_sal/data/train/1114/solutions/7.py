for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    i = 1
    while i < n - 1 and a[i] == a[i + 1]:
        i += 1
    if a[0] == a[1]:
        print(i * (i + 1) / (n * (n - 1)))
    else:
        print(2 * i / (n * (n - 1)))

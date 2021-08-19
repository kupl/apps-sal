t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    valid = False
    if n % 2 == 1 and a[0] == 1:
        for j in range(int((n - 1) / 2)):
            if a[j] == a[n - 1 - j]:
                valid = True
            if a[j] + 1 != a[j + 1]:
                valid = False
            if a[n - 1 - j] != a[n - 2 - j] - 1:
                valid = False
    if valid:
        print('yes')
    else:
        print('no')

def func(a):
    a.sort()
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] + a[j] == 2000:
            return 'Accepted'
        elif a[i] + a[j] > 2000:
            j -= 1
        else:
            i += 1
    return 'Rejected'


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(func(a))

(n, t) = list(map(int, input().split()))
while t:
    t -= 1
    a = list(map(int, input().split()))
    i = n - 1
    while i > 0 and a[i] < a[i - 1]:
        i -= 1
    j = i
    i -= 1
    mini = j
    while j < n:
        if a[j] > a[i] and a[j] < a[mini]:
            mini = j
        j += 1
    (a[i], a[mini]) = (a[mini], a[i])
    a[i + 1:] = sorted(a[i + 1:])
    print(*a)

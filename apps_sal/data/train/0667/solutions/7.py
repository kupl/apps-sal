try:
    x = int(input())
    for _ in range(x):
        b = list(map(int, input().split()))
        a = list(map(int, input().split()))
        y = b[1]
        j = len(a) - 1
        while j >= 0:
            y = a[j] * int(y / a[j])
            j -= 1
        print(y)
except:
    pass

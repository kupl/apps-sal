for _ in range(int(input())):
    a = list(map(int, input().split()))
    p = a[len(a) - 1]
    b = sum(a) - p
    if(b * p - 120 > 0):
        print("Yes")
    else:
        print("No")

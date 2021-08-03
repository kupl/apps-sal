for _ in range(int(input())):
    a = input().split()
    n = int(a[0])
    k = int(a[1])
    if n % (k * k):
        print("YES")
    else:
        print("NO")

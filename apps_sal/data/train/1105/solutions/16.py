for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if(n == 1):
        print(a[0])
    elif(n == 2):
        print(max(a[0], a[1]))
    else:
        b = a[n - 1]
        c = a[n - 2]
        for i in range(n - 3, -1, -1):
            if(c < b):
                c += a[i]
            else:
                b += a[i]
        if(c < b):
            print(b)
        else:
            print(c)

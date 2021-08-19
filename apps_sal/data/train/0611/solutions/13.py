try:
    t = int(input())
    for i in range(t):
        n = int(input())
        z = 0
        a = [int(j) for j in input().split(' ')]
        for k in range(n - 1):
            for x in range(k + 1, n):
                if a[k] != a[x]:
                    if a[a[k] - 1] == a[a[x] - 1]:
                        print('Truly Happy')
                        z = 1
                        break
            if z == 1:
                break
        if z == 0:
            print('Poor Chef')
except:
    pass

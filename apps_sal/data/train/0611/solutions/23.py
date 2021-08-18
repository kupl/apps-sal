for i in range(int(input())):
    c = 0
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        for j in range(len(a)):
            try:
                if a[i] != a[j] and a[a[i] - 1] == a[a[j] - 1]:
                    c += 1
                else:
                    pass
            except:
                pass
    if c == 0:
        print('Poor Chef')
    else:
        print('Truly Happy')

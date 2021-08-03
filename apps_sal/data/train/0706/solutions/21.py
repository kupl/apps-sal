try:
    for t in range(int(input())):
        n, k = list(map(int, input().split()))
        l = list(map(int, input().split()))
        c = 0
        z = k
        for j in range(0, n):
            if(l[j] <= z):
                z = z - l[j]
                if(j + 1 < n and l[j + 1] > z):
                    z = k
                    c = c + 1
            else:
                c = -2
                break
        if(c == -2):
            print(-1)
        else:
            print(c + 1)
except EOFError as e:
    pass
    # TODO: write code...

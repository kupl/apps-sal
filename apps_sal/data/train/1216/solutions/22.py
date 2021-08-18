try:
    for i in range(int(input())):
        n, x = map(int, input().split())
        l = list(map(int, input().strip().split()))
        l.sort()

        for i in l:
            if (i >= x):
                print("YES")
                break
        else:
            print("NO")
except:
    pass

try:
    for i in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        k = []
        for i in l:
            if i > 1:
                k.append(i)
        two = k.count(2)
        c2 = len(k) - two
        print(two * c2 + c2 * (c2 - 1) // 2)
except:
    pass

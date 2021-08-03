try:
    t = int(input())
    while(t > 0):
        t -= 1
        n = int(input())
        check = {}
        sm = 0
        for i in range(n):
            st, bl = input().split(' ')
            if st in check:
                if bl == '0':
                    check[st][0] += 1
                else:
                    check[st][1] += 1
            else:
                if bl == '0':
                    check[st] = [1, 0]
                else:
                    check[st] = [0, 1]
        for i in check:
            sm = sm + max(check[i])
        print(sm)
except EOFError:
    pass

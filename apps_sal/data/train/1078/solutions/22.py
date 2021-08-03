# cook your dish here
try:
    T = int(input())
    for t in range(T):

        w = list(map(int, input().split()))
        s = w.pop(0)
        c = 0
        # print(w,s)
        while len(w) > 0:
            r = s
            c += 1
            # print(c,w)
            if w[0] > w[-1]:
                while len(w) > 0 and r >= w[0]:
                    r -= w[0]
                    w.pop(0)
            else:
                while len(w) > 0 and r >= w[-1]:
                    r -= w[-1]
                    w.pop(-1)
        print(c)
except:
    pass

try:
    t = int(input())
    for __ in range(t):
        (N, m) = map(int, input().split())
        A = []
        dic = {}
        for i in range(N - 1):
            (a, b) = map(int, input().split())
            if a in dic:
                dic[a] += str(b) + ','
            else:
                dic[a] = str(b) + ','
            if b in dic:
                dic[b] += str(a) + ','
            else:
                dic[b] = str(a) + ','
        for _ in range(m):
            (term1, dist1, term2, dist2) = map(str, input().split())
            l = [term1]
            A = []

            def distance(t, c, x, A, l):
                if t == int(c):
                    A += [x]
                else:
                    string = ''
                    for i in dic[int(x)]:
                        if i == ',':
                            if string not in l:
                                l += [string]
                                x = string
                                distance(t + 1, c, x, A, l)
                                string = ''
                            else:
                                string = ''
                        else:
                            string += str(i)
            distance(0, dist1, term1, A, l)
            l1 = []
            for i in A:
                if i != term1:
                    l1 += [i]
            A = []
            l = [term2]
            distance(0, dist2, term2, A, l)
            l2 = []
            for i in A:
                if i != term2:
                    l2 += [i]
            count = 0
            for i in l1:
                if i in l2:
                    if count < 1:
                        print(int(i))
                        count += 1
            if count == 0:
                print(-1)
except:
    pass

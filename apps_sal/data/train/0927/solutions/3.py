try:
    def performOperations(N, op):
        a = [i for i in range(1, N + 1)]
        m = set(a)
        s = sum(a)
        ans = []
        for i in op:
            if i in m:
                a[0], a[N - 1] = a[N - 1], a[0]
            else:
                s -= a[N - 1]
                s += i
                m.remove(a[N - 1])
                m.add(i)
                a[N - 1] = i
            ans.append(s)
        return ans
    op = []
    N, m = map(int, input().split())
    for _ in range(m):
        op.append(int(input()))
    answ = performOperations(N, op)
    for i in answ:
        print(i)


except EOFError as error:
    pass

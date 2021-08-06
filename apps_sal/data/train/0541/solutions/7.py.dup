for t in range(int(input())):
    n = int(input())
    l = [int(j) - 1 for j in input().split()]
    d = dict()
    # st = tuple([0 for i in range(30)])
    st = 0
    d[st] = -1
    ans = 1
    for i in range(n):
        # st = list(st)
        st = st ^ (1 << l[i])
        # st[l[i]] = 1-st[l[i]]
        for j in range(30):
            # st1 = list(st)
            st1 = st
            st1 = st1 ^ (1 << j)
            # st1[j] = 1 - st1[j]
            if st1 in d and d[st1] != i - 1:
                ans = max(ans, i - d[st1])
                # print(i, d[tuple(st1)])
        if st not in d:
            d[st] = i

    print(ans // 2)

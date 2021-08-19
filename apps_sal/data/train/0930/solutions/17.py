try:
    # cook your code here
    for _ in range(int(input())):
        N = int(input())
        X = list(range(1, N + 1)) + list(range(N - 1, 0, -1))
        A = [[] for i in range(N)]
        count = 1
        start = 0
        # print(X)
        for x in range(len(X)):
            if x > N - 1:
                start += 1
            # print(A,start,X[x],count)
            for i in range(start, start + X[x]):
                A[i].append(count)
                count += 1
        for a in A:
            print(*a)
        # print(X)

        # print(A)
        # for a in A:
        #     print(*a)


except:
    pass

import itertools
for _ in range(int(input())):
    N = int(input())
    A = list()
    for i in range(N):
        B = list(map(int, input().split(" ")))
        A.append(B)
    C = list(itertools.chain.from_iterable(A))
    Z = C.count(0)
    temp = N - 1
    for i in range(N - 1):
        y = int((N - 1 - i) * (N - i))
        if Z >= y:
            temp = i
            break
    print(temp)

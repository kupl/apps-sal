for _ in range(int(input())):
    N = int(input())
    A = {}
    for i in range(N):
        (w, s) = input().split()
        s = int(s)
        if w not in A:
            A[w] = [1, 0] if s == 0 else [0, 1]
        elif s == 0:
            A[w][0] += 1
        else:
            A[w][1] += 1
    c = 0
    for i in A.values():
        c += max(i)
    print(c)

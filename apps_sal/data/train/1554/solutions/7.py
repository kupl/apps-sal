def fun(M, B):
    if M == B:
        return M * 2
    elif M == 0:
        return B * 2
    elif B == 0:
        return M * 2
    else:
        if M > B:
            return fun(M % B, B)
        else:
            return fun(M, B % M)


t = int(input())
for i in range(t):
    M, B = list(map(int, input().split()))

    print(fun(M, B))

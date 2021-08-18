import string

ASCII_ASC = string.ascii_lowercase
ASCII_DSC = sorted(ASCII_ASC, reverse=True)


def int_input():
    return int(input())


def array_input(data_type=int):
    if data_type != str:
        return list(map(data_type, input().split("")))
    else:
        return list(map(str, input()))


def solve():
    N = int_input()
    A = array_input(data_type=str)
    B = array_input(data_type=str)
    for i in range(N):
        if A[i] < B[i]:
            print(-1)
            return
    res = []
    for ch in ASCII_DSC:
        idx_pos = []
        chk = False

        for i in range(0, N):
            if B[i] == ch and A[i] != ch:
                idx_pos.append(i)
        if chk is False and len(idx_pos):
            for i in range(0, N):
                if A[i] == ch:
                    chk = True
                    idx_pos.append(i)
        if chk is False and len(idx_pos):
            print(-1)
            return
        if len(idx_pos):
            res.append(idx_pos)
        for idx in idx_pos:
            A[idx] = ch
    print(len(res))
    for arr in res:
        print(len(arr), " ".join(map(str, arr)))


t = int_input()
while t > 0:
    t -= 1
    solve()

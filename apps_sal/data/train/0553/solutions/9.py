import sys


def fop(s, end='\n'):
    sys.stdout.write(str(s) + end)


def fip():
    return sys.stdin.readline().strip()


def fintinp():
    return int(fip())


def flistinp(func=int):
    return list(map(func, fip().split()))


def fnsepline(n, func=str):
    return [func(fip()) for _ in range(n)]


def byeqs(pqr, abc):
    (p, q, r) = pqr
    (a, b, c) = abc
    muls = []
    try:
        if p != q:
            m_ = (a - b) // (p - q)
            muls.append(m_)
    except:
        pass
    try:
        if p != r:
            m_ = (a - c) // (p - r)
            muls.append(m_)
    except:
        pass
    try:
        if q != r:
            m_ = (b - c) // (q - r)
            muls.append(m_)
    except:
        pass
    return muls


def recSolver(pqr, abc, ans=0):
    if pqr == abc:
        return ans
    if ans >= 2:
        return 3
    adds = [abc[i] - pqr[i] for i in range(3)]
    muls = [abc[i] // pqr[i] if pqr[i] != 0 else 0 for i in range(3)] + byeqs(pqr, abc)
    f_ans = 3
    for ss in range(8):
        for a in adds:
            pqr_copy = list(pqr)
            for i in [1, 2, 4]:
                if ss & i:
                    pqr_copy[i >> 1] += a
            f_ans = min(f_ans, recSolver(pqr_copy, abc, ans + 1))
        for m in muls:
            pqr_copy = list(pqr)
            for i in [1, 2, 4]:
                if ss & i:
                    pqr_copy[i >> 1] *= m
            f_ans = min(f_ans, recSolver(pqr_copy, abc, ans + 1))
    return f_ans


for _ in range(fintinp()):
    pqr = flistinp()
    abc = flistinp()
    fop(recSolver(pqr, abc, 0))

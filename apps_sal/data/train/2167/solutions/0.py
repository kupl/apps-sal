def read_data():
    n, q = map(int, input().split())
    As = list(map(int, input().split()))
    LRs = []
    for i in range(q):
        L, R = list(map(int, input().split()))
        LRs.append((L, R))
    return n, q, As, LRs

def solve(n, q, As, LRs):
    difs = calc_difs(As)
    Ls = get_Ls(difs)
    Rs = get_Rs_allow_ties(difs)
    for L, R in LRs:
        print(calc(L-1, R-2, Ls, Rs, difs))

    
def calc_difs(As):
    difs = [abs(a0 - a1) for a0, a1 in zip(As, As[1:])]
    return difs


def get_Ls(Vs):
    L = []
    st = []
    for i, v in enumerate(Vs):
        while st and Vs[st[-1]] < v:
            st.pop()
        if st:
            L.append(st[-1] + 1)
        else:
            L.append(0)
        st.append(i)
    return L

def get_Ls_allow_ties(Vs):
    L = []
    st = []
    for i, v in enumerate(Vs):
        while st and Vs[st[-1]] <= v:
            st.pop()
        if st:
            L.append(st[-1] + 1)
        else:
            L.append(0)
        st.append(i)
    return L

def get_Rs(Vs):
    n = len(Vs)
    revVs = Vs[::-1]
    revRs = get_Ls(revVs)
    revRs.reverse()
    return [n - 1 - R for R in revRs]


def get_Rs_allow_ties(Vs):
    n = len(Vs)
    revVs = Vs[::-1]
    revRs = get_Ls_allow_ties(revVs)
    revRs.reverse()
    return [n - 1 - R for R in revRs]

def calc(L, R, Ls, Rs, difs):
    ans = 0
    for i in range(L, R + 1):
        ans += difs[i] * (i - max(Ls[i], L) + 1) * (min(Rs[i], R) - i + 1)
    return ans

n, q, As, LRs = read_data()
solve(n, q, As, LRs)

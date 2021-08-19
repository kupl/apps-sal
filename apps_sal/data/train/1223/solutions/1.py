T = eval(input())


def diff(seqA, seqB):
    d = 0
    for i in range(len(seqA)):
        d += abs(seqA[i] - seqB[i])
    return d


def gen_seq(start, L, N):
    return [start + i * L for i in range(N)]


def binSearch(s, e, ll, L, N):
    if s == e:
        return diff(ll, gen_seq(s, L, N))
    mid = int((s + e) / 2)
    if diff(ll, gen_seq(mid, L, N)) > diff(ll, gen_seq(mid + 1, L, N)):
        return binSearch(mid + 1, e, ll, L, N)
    else:
        return binSearch(s, mid, ll, L, N)


while T > 0:
    T -= 1
    (N, L, A, B) = list(map(int, input().split()))
    ll = list(map(int, input().split()))
    ll = sorted(ll)
    lastpossible = B - L
    startA = A
    lastA = int(B - L - (N - 1) * L)
    seq_cost_beg = diff(ll, gen_seq(startA, L, N))
    seq_cost_end = diff(ll, gen_seq(lastA, L, N))
    print(binSearch(startA, lastA, ll, L, N))

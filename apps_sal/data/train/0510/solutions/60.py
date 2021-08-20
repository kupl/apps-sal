from collections import defaultdict
from bisect import bisect_left, bisect_right, insort_left, insort_right
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    S = list(input())
    q = int(input())
    Q = [input() for _ in range(q)]
    dd = defaultdict(list)
    for i in range(ord('a'), ord('z') + 1):
        dd[chr(i)] = []
    for (i, st) in enumerate(S):
        dd[st].append(i)
    ans = []
    for q in Q:
        (t, a, b) = q.split()
        a = int(a) - 1
        if int(t) == 1:
            if S[a] == b:
                continue
            id = bisect_left(dd[S[a]], a)
            dd[S[a]].pop(id)
            insort_left(dd[b], a)
            S[a] = b
        else:
            b = int(b) - 1
            cnt = 0
            for l in dd.values():
                if l and a <= l[-1] and (l[bisect_left(l, a)] <= b):
                    cnt += 1
            ans.append(cnt)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()

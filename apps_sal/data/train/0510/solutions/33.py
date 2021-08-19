from bisect import bisect_left, insort_left
import sys
readline = sys.stdin.readline


def main():
    n = int(readline())
    s = list(readline().rstrip())
    q = int(readline())
    chk_abc = [[] for i in range(26)]
    for (i, si) in enumerate(s):
        ci = ord(si) - 97
        chk_abc[ci].append(i)
    ans = []
    for _ in range(q):
        (cmd, i, j) = readline().rstrip().split()
        i = int(i) - 1
        if cmd == '1':
            if s[i] == j:
                continue
            c1 = ord(s[i]) - 97
            prev = chk_abc[c1]
            c2 = ord(j) - 97
            prev.pop(bisect_left(prev, i))
            s[i] = j
            insort_left(chk_abc[c2], i)
        else:
            j = int(j) - 1
            num = 0
            for chk in chk_abc:
                le = len(chk)
                k = bisect_left(chk, i, 0, le)
                if k == le:
                    continue
                if i <= chk[k] <= j:
                    num += 1
            ans.append(num)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()

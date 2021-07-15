def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left, insort_left
    N = int(input())
    S = list(input())
    Q = int(input())
    dic = {chr(i): [] for i in range(ord('a'), ord('z')+1)}
    for i in range(N):
        dic[S[i]].append(i)
    for _ in range(Q):
        query, a, c = input().split()
        if query == "1":
            i = int(a)-1
            if S[i] == c:
                continue
            ind = bisect_left(dic[S[i]], i)
            dic[S[i]].pop(ind)
            insort_left(dic[c], i)
            S[i] = c
        else:
            l, r = int(a)-1, int(c)-1
            ans = 0
            for inds in dic.values():
                if inds and l <= inds[-1] and inds[bisect_left(inds, l)] <= r:
                    ans += 1
            print(ans)

def __starting_point():
    main()
__starting_point()

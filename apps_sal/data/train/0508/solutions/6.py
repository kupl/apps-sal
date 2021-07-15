from bisect import bisect_left
def main():
    N, Q = map(int, input().split())
    W = [tuple(map(int, input().split())) for _ in range(N)]
    W.sort(key=lambda x:x[2])
    
    D = [int(input()) for _ in range(Q)]
    ans = [-1]*Q
    skip = [-1]*Q
    for s, t, x in W:
        l = bisect_left(D, s-x)
        r = bisect_left(D, t-x)
        while l < r:
            if skip[l] == -1:
                ans[l] = x
                skip[l] = r
                l+=1
            else:
                l = skip[l]
    for a in ans:
        print(a)
main()  

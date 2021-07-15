import sys
input = sys.stdin.readline

Q = int(input())
Query = [list(input().rstrip()) for _ in range(Q)]


for S in Query:
    tmp = 0
    ans = 0
    for i, s in enumerate(S):
        if s == "L":
            tmp += 1
        else:
            ans = max(tmp+1, ans)
            tmp = 0
    ans = max(tmp+1, ans)
    print(ans)

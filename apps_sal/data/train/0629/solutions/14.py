# cook your dish here
t = int(input())
for i in range(t):
    [r, g, b, k] = list(map(int, input().split()))
    rs = list(map(int, input().split()))
    bs = list(map(int, input().split()))
    gs = list(map(int, input().split()))
    ans = sorted([max(rs), max(bs), max(gs)])
    for i in range(k):
        ans[-1] = int(ans[-1] / 2)
        ans = sorted(ans)
    print(ans[-1])

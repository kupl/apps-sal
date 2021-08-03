import sys
input = sys.stdin.readline
maxn = 100005
hell = 1000000007
vis = [0] * 3 * maxn


def meowmeow321():
    n, m = map(int, input().split())
    for i in range(3 * n + 1):
        vis[i] = 0
    elst = []
    for i in range(m):
        x, y = map(int, input().split())
        if (not vis[x]) and (not vis[y]):
            vis[x] = 1
            vis[y] = 1
            elst.append(i + 1)
    if len(elst) >= n:
        print("Matching")
        for i in range(n):
            print(elst[i], end=" ")
        print("")
    else:
        print("IndSet")
        cnt = 0
        cur = 1
        while cnt < n and cur <= 3 * n:
            if not vis[cur]:
                print(cur, end=" ")
                cnt += 1
            cur += 1
        print("")


t = int(input())
for xxx in range(t):
    meowmeow321()

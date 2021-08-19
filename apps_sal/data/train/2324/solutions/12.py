import sys
sys.setrecursionlimit(10**6)
N = int(input())
I = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    I[a - 1].append(b - 1)
    I[b - 1].append(a - 1)


def path(s, t, pth, visited):  # sからtに至るpathを求める pth = list(), visited = set()
    pth.append(s)
    if s == t:
        return (pth, True)
    visited.add(s)
    flag = False
    for q in I[s]:
        if q not in visited:
            pth, flag = path(q, t, pth, visited)
            if flag:
                return (pth, True)
    pth.pop()
    return (pth, False)


def count(s, d, visited):  # グラフをsを含み、dを含まない最大の連結成分に制限した時の要素数
    visited.add(s)
    for q in I[s]:
        if q not in visited and q != d:
            visited = count(q, d, visited)
    return visited


pth, flag = path(0, N - 1, [], set())

if not flag:
    print("error")
d = pth[(len(pth) + 1) // 2]
n = len(count(0, d, set()))
#print(pth, flag, d)

if n > N // 2:
    print("Fennec")
else:
    print("Snuke")

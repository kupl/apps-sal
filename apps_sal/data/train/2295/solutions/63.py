"""
すべて等しかったら0
それ以外は A > B を満たすものの内最小の黒以外取れる
"""
N = int(input())
ans = 0
l = []
for i in range(N):
    (A, B) = list(map(int, input().split()))
    ans += A
    if A > B:
        l.append(B)
if len(l) == 0:
    print(0)
else:
    l.sort()
    print(ans - l[0])

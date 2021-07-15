import sys
input = sys.stdin.readline
import math

"""
内部の点が絡むものは、曲線で結んでホモトピーで変形すれば、無視できる
境界の2点を結ぶものたちだけが問題
"""

R,C,N = map(int,input().split())
pts = [] # 角度、番号
is_inner = lambda x,y:  0 < x < R and 0 < y < C
for i in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    if is_inner(x1,y1) or is_inner(x2,y2):
        continue
    pts.append((math.atan2(y1 - C/2, x1 - R/2),i))
    pts.append((math.atan2(y2 - C/2, x2 - R/2),i))
pts.sort()

arr = []
for _, i in pts:
    if arr and arr[-1] == i:
        arr.pop()
        continue
    arr.append(i)

answer = 'NO' if arr else 'YES'
print(answer)

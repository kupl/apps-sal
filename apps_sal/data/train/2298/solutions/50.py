"""
import math
a, b = map(str, input().split())
j = int(a + b)
if math.sqrt(j).is_integer():
    print("Yes")
else:
    print("No")
"""
'\nans = ["Positive","Negative"]\na, b = map(int, input().split())\nif 0 < a:\n    print("Positive")\nelif b >= 0:\n    print("Zero")\nelse:\n    print(ans[(b-a)%2-1])\n'
'\nimport itertools\nn = int(input())\nMARCH = ["M", "A", "R", "C", "H"]\nmarch = [0 for _ in range(5)]\nfor i in range(n):\n    s = input()\n    if s[0] in MARCH:\n        march[MARCH.index(s[0])] += 1\nnum = list(range(5))\na = list(itertools.combinations(num, 3))\nans = 0\nfor i in a:\n    bf = 1\n    for k in i:\n        bf *= march[k]\n    ans += bf\nprint(ans)\n'
'\nn = int(input())\nD = [list(map(int, input().split())) for _ in range(n)]\nq = int(input())\np = [int(input()) for _ in range(q)]\nans = [[0 for i in range(n)] for _ in range(n)]\nfor i in range(n):\n    for j in range(n):\n        break\nfor _ in p:\n    print(ans[p])\n'
'\ns = input()\nbf = s[0]\nans = 0\nfor i in range(1,len(s)):\n    if bf != s[i]:\n        ans += 1\n        bf = s[i]\nprint(ans)\n'
'\nn = int(input())\nta = [list(map(int, input().split())) for _ in range(n)]\nans = ta[0]\nfor i in ta:\n    if ans[0] <= i[0] and ans[1] <= i[1]:\n        ans = i\n    else:\n        a = ((ans[0] - 1) // i[0]) + 1\n        b = ((ans[1] - 1) // i[1]) + 1\n        ab = max(a,b)\n        ans = [i[0] * ab, i[1] * ab]\nprint(ans[0]+ans[1])\n'
(n, t) = map(int, input().split())
a = list(map(int, input().split()))
minv = a[0]
maxv = 0
ans = 0
for i in range(1, n):
    if maxv == a[i] - minv:
        ans += 1
    elif maxv < a[i] - minv:
        maxv = a[i] - minv
        ans = 1
    else:
        minv = min(minv, a[i])
print(ans)
'\ns = input()\nans = 0\nfor i in range(1,len(s)):\n    if i % 2 == 1:\n        if s[i] != "p":\n            ans += 1\n    else:\n        if s[i] != "g":\n            ans -= 1\nprint(ans)\n'

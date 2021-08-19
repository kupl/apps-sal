# cook your dish here
import sys
sys.setrecursionlimit(10**8)
try:
    for _ in range(int(input())):
        class mat(object):
            limit = []
            arr = []
            num = 0
            ans = 0

        def passes(n, m):
            if m > mat.num:
                return
            mat.ans += 1
            mat.limit.append(m)
            for i in range(1, mat.arr[m] + 1):
                if m - i > 0 and n < mat.num - 1 and not(m - i in mat.limit):
                    passes(n + 1, m - i)
                if m + i < mat.num and n < mat.num - 1 and not(m + i in mat.limit):
                    passes(n + 1, m + i)
            mat.limit.pop()
        mat.num = int(input())
        mat.arr = [] * mat.num
        mat.arr = list(map(int, input().split()))
        passes(0, 0)
        print(mat.ans)

except:
    pass

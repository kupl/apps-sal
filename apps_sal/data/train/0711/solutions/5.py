# from sys import stdin, stdout
# from math import floor, gcd, fabs, factorial, fmod, sqrt, inf, log
# from collections import defaultdict as dd, deque
# from heapq import merge, heapify, heappop, heappush, nsmallest
# from bisect import bisect_left as bl, bisect_right as br, bisect
# mod = pow(10, 9) + 7
# mod2 = 998244353
# def inp(): return stdin.readline().strip()
# def out(var, end="\n"): stdout.write(str(var)+"\n")
# def outa(*var, end="\n"): stdout.write(' '.join(map(str, var)) + end)
# def lmp(): return list(mp())
# def mp(): return map(int, inp().split())
# def smp(): return map(str, inp().split())
# def l1d(n, val=0): return [val for i in range(n)]
# def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]
# def remadd(x, y): return 1 if x%y else 0
# def ceil(a,b): return (a+b-1)//b

# def isprime(x):
#     if x<=1: return False
#     if x in (2, 3): return True
#     if x%2 == 0: return False
#     for i in range(3, int(sqrt(x))+1, 2):
#         if x%i == 0: return False
#     return True
    
# def bitmsk(s):
#     md = {}
#     S = "abcdefghijklmnopqrstuvwxyz"
#     for i in S:
#         md[i]=0
#     for i in s:
#         if i in md: md[i]+=1
#     b = ""
#     for i in S:
#         b+='1' if md[i]%2 else '0'
#     return b

# def xor(a, b):
#     c = ""
#     for i in range(27):
#         if (a[i]=='0' and b[i]=='0') or (a[i]=='1' and b[i]=='1'): c += '0'
#         else: c += '1'
#     return c

# for _ in range(int(inp())):
#     s = inp()
#     l = len(s)
#     b = bitmsk(s)
#     b += '0'
#     good = []
#     good.append(b)
#     b = b[:-1]
#     for i in range(26):
#         x = '1' if b[i]=='0' else '0'
#         good.append(b[:i]+x+b[i+1:]+'1')
#     pre = ['0'*27]
#     cq = 0
#     mdd = {}
#     for i in range(l):
#         if s[i]=='?': cq+=1
#         k = '1' if cq%2 else '0'
#         kk = bitmsk(s[:i+1])+k
#         pre.append(kk)
#         if kk in mdd: mdd[kk].append((i+1))
#         else: mdd[kk]=[(i+1)]
#     # print(pre)
#     ans = 0
#     for i in range(l):
#         # for j in range(i+1, l+1):
#         #     if xor(pre[i], pre[j]) in good:
#         #         ans += 1
#         for j in good:
#             xx = xor(pre[i], j)
#             if xx in mdd:
#                 ans += len(mdd[xx])-br(mdd[xx], i)
#     out(ans)

# cook your dish here
from sys import stdin, stdout
from math import floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from collections import defaultdict as dd, deque
from heapq import merge, heapify, heappop, heappush, nsmallest
from bisect import bisect_left as bl, bisect_right as br, bisect
mod = pow(10, 9) + 7
mod2 = 998244353
def inp(): return stdin.readline().strip()
def out(var, end="\n"): stdout.write(str(var)+"\n")
def outa(*var, end="\n"): stdout.write(' '.join(map(str, var)) + end)
def lmp(): return list(mp())
def mp(): return map(int, inp().split())
def smp(): return map(str, inp().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]
def remadd(x, y): return 1 if x%y else 0
def ceil(a,b): return (a+b-1)//b

def isprime(x):
    if x<=1: return False
    if x in (2, 3): return True
    if x%2 == 0: return False
    for i in range(3, int(sqrt(x))+1, 2):
        if x%i == 0: return False
    return True
    
def xor(a, b):
    c = ""
    for i in range(27):
        if (a[i]=='0' and b[i]=='0') or (a[i]=='1' and b[i]=='1'): c += '0'
        else: c += '1'
    return c

for _ in range(int(inp())):
    s = inp()
    l = len(s)
    md = {}
    S = "abcdefghijklmnopqrstuvwxyz"
    for i in S:
        md[i]=0
        
    cq = 0
    mdd = {}
    pre = ['0'*27]
    for i in range(l):
        if s[i] in md: md[s[i]]+=1
        b = ""
        for j in S:
            b+='1' if md[j]%2 else '0'
        if s[i]=='?': cq+=1
        k = '1' if cq%2 else '0'
        kk = b+k
        pre.append(kk)
        if kk in mdd: mdd[kk].append((i+1))
        else: mdd[kk]=[(i+1)]
        
    b = pre[-1]
    good = []
    good.append(b[:-1]+'0')

    b = b[:-1]
    for i in range(26):
        x = '1' if b[i]=='0' else '0'
        good.append(b[:i]+x+b[i+1:]+'1')
    alpha = {}
    S = "abcdefghijklmnopqrstuvwxyz?"
    for i in range(27):
        alpha[S[i]] = i
    
    ans = 0
    for j in good:
        prev = j
        for i in range(l+1):
            if i != 0:
                x = alpha[s[i-1]]
                kk = '0' if prev[x] == '1' else '1'
                prev = prev[:x]+kk+prev[x+1:]
            if prev in mdd:
                ans += len(mdd[prev])-br(mdd[prev], i)
    out(ans)

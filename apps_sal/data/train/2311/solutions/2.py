from collections import defaultdict
import sys
def f(n): # O(digits)
    out = 1
    while(n > 0):
        digit = n % 10
        if digit != 0:
            out *= digit
        n = n//10
    return out

memorization = defaultdict(int) # For much faster calculation g(n)
def g(n):
    if n < 10:return n
    f_n = f(n)
    if f_n in memorization:
        return memorization[f_n]
    else:
        ans = g(f_n)
        memorization[f_n] = ans
        return ans

def s(L,l,r,k):
    if l > r:return l
    m = (l+r)//2
    if L[m] == k:return m
    if L[m] > k:return s(L,l,m-1,k)
    else:return s(L,m+1,r,k)

ans = {i : [1000001] for i in range(1,10)}

for i in range(1,1000001): # O(n) because 9*9*9*9*9*9 = 531441 -> Maxnimum each number between [1,531441] will calculated only once
    g_i = g(i)             # due to memorization
    if g_i != 0:ans[g_i].append(i)    
for i in ans: # O( nlog(n) )
    ans[i].sort()

input = sys.stdin.readline
n = int(input())
for i in range(n): # O( Qlog(n) )
    l,r,k = [int(i) for i in input().split()] #O (logn) for each Q
    l_idx,r_idx = s(ans[k],0,len(ans[k])-1,l) , s(ans[k],0,len(ans[k])-1,r)
    #FIX l_idx to Upper_bound
    if ans[k][l_idx] != l and ans[k][l_idx] < l and ans[k][l_idx+1] > l : l_idx += 1
    #FIX r_idx to Lower_bound
    if ans[k][r_idx] != r and not (ans[k][r_idx] < r and ans[k][r_idx+1] > r) : r_idx -= 1
    print(r_idx - l_idx + 1)
    


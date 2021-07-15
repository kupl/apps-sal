class Solution(object):
     # Rabin-Karp Algorithm (rolling hash)
     def repeatedStringMatch1(self, A, B):
         """
         :type A: str
         :type B: str
         :rtype: int
         """
         def check(index):
             return all(A[(i+index) % len(A)] == c
                    for i, c in enumerate(B))
 
         M, p = 10**9+7, 113
         p_inv = pow(p, M-2, M)
         q = (len(B)+len(A)-1) // len(A)
 
         b_hash, power = 0, 1
         for c in B:
             b_hash += power * ord(c)
             b_hash %= M
             power = (power*p) % M
 
         a_hash, power = 0, 1
         for i in range(len(B)):
             a_hash += power * ord(A[i%len(A)])
             a_hash %= M
             power = (power*p) % M
 
         if a_hash == b_hash and check(0): return q
 
         power = (power*p_inv) % M
         for i in range(len(B), (q+1)*len(A)):
             a_hash = (a_hash-ord(A[(i-len(B))%len(A)])) * p_inv
             a_hash += power * ord(A[i%len(A)])
             a_hash %= M
             if a_hash == b_hash and check(i-len(B)+1):
                 return q if i < q*len(A) else q+1
 
         return -1
     #KMP
     def repeatedStringMatch(self, A, B):
         """
         :type A: str
         :type B: str
         :rtype: int
         """
  
         def get_fail(s):
             f = [0] * (len(s) + 1)
             for i in range(1, len(s)):
                 j = f[i]
                 while j and s[i] != s[j]: j = f[j]
                 if s[i] == s[j]: j += 1
                 f[i + 1] = j
             return f
  
         # kmp
         f = get_fail(B)
         j = 0
         vis = {0}
         cnt = 1
         while True:
             for i in range(len(A)):
                 while j and A[i] != B[j]: j = f[j]
                 if A[i] == B[j]: j += 1
                 if j == len(B):
                     return cnt
             if j in vis: return -1 
             vis.add(j)
             cnt += 1
         return -1
 
     
     


class Solution:
     def repeatedStringMatch(self, A, B):
         k = int(len(B) / len(A))
         m = ""
         h = A + A[0]
         for i in range(len(B)-1):
             if B[i:i+2] not in h: return -1
         for i in range(k):
             m += A
         while B not in m:
             m += A
             k += 1
             if k>100: return -1
         return k


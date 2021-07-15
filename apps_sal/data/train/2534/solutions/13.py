class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = [0 for ii in range(n)]
        ones = [0 for ii in range(n)]
        if s[0] == '0':
            zeros[0] = 1
        else:
            zeros[0] = 0
        if s[n-1] == '1':
            ones[n-1] = 1
        else:
            ones[n-1] = 0
        
        for ii in range(1,n):
            if s[ii] == '0':
                zeros[ii] = zeros[ii-1] + 1
            else:
                zeros[ii] = zeros[ii-1]
            
            if s[n - 1 - ii] == '1':
                ones[n-1-ii] = ones[n-ii] + 1
            else:
                ones[n-1-ii] = ones[n-ii]
                
        if s[0] == '1':
            ones[0] -= 1
        if s[n-1] == '0':
            zeros[n-1] -= 1
          
        mx = 0
        for ii in range(len(zeros)):
            if zeros[ii] + ones[ii] > mx:
                mx = zeros[ii] + ones[ii]
                
        return mx

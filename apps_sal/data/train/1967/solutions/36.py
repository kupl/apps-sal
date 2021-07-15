class Solution:
    def splitIntoFibonacci(self, S):
        upper_limit = 2 ** 31 - 1
        def split_fib(s, res):
            if s == \"\"  and len(res) > 2 and int(res[-1]) == int(res[-2]) + int(res[-3]):
                return True
            if len(res) > 2 and int(res[-1]) != int(res[-2]) + int(res[-3]):
                return False
            if int(res[-1]) >= upper_limit:
                return False
            
            for i in range(1, len(s)+1):
                if (i > 1 and s[:i][0] == '0'):
                    continue
                res.append(s[:i])
                if split_fib(s[i:], res):
                    return True
                res.pop()
            return False

        res = []
        for i in range(1, len(S)):
            if S[:i][0] == '0' and i > 1:
                continue
            res.append(S[:i])
            if split_fib(S[i:], res) and int(res[-1]) <= upper_limit:
                return res
            res.pop()
        return []
        

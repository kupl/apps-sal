class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = ''
        for i in range(1,len(str(n))+1):
            res = str(n)[::-1][i-1] + res
            if(i%3 == 0 and i != len(str(n))):
                res = '.' + res
        return res


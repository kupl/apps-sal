class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        if n < 2:
            return []
        if n == 2:
            return ['1/2']
        ans = []
        record = {}
        for i in range(2, n):
            a = 1
            b = i
            while b <= n:
                for c in range(1, b):
                    if c / b not in record:
                        ans.append('{}/{}'.format(c, b))
                        record[c / b] = True
                b += 1
        return ans

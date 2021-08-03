class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = []
        for op in ops:
            try:
                integer = int(op)
            except ValueError:
                if op == 'C':
                    ans.pop()
                elif op == 'D':
                    ans.append(ans[-1] * 2)
                else:
                    ans.append(sum(ans[-2:]))
            else:
                ans.append(integer)
        return sum(ans)

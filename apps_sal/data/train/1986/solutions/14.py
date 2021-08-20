class Solution:

    def helper(self, n):
        if n == 1:
            return ['0', '1']
        else:
            res = self.helper(n - 1)
            return ['0' + x for x in res] + ['1' + x for x in res[::-1]]

    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray_code = ['0', '1']
        n -= 1
        while n > 0:
            gray_code = ['0' + x for x in gray_code] + ['1' + x for x in gray_code[::-1]]
            n -= 1
        gray_code = [int(x, 2) for x in gray_code]
        return gray_code[gray_code.index(start):] + gray_code[:gray_code.index(start)]

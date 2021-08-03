class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        outputs = []

        for i in range(2, n + 1):
            for j in range(1, i):
                if self._gcd(i, j) == 1:
                    outputs.append(f'{j}/{i}')

        return outputs

    def _gcd(self, i: int, j: int):
        if i > j:
            i, j = j, i
        res = j % i
        if res == 0:
            return i
        else:
            return self._gcd(i, res)

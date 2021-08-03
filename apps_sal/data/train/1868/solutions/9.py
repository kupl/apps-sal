class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        return [i for i in [int('{:010b}'.format(i)[::-1], 2) for i in range(1, 1 << 10)] if i <= N]

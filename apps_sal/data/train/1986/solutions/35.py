class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        used = set()
        result = [None] * int(2**n)
        result[0] = start
        used.add(start)
        for i in range(1, len(result)):
            for x in range(n):
                bit = bool(result[i - 1] & (1 << x))
                if bit:
                    val = result[i - 1] - (1 << x)
                else:
                    val = result[i - 1] + (1 << x)
                if val not in used:
                    used.add(val)
                    result[i] = val
                    break
        return result

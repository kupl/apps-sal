class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        maos = {x: 0 for x in set(A)}
        for x in A:
            maos[x] += 1
        for x in maos:
            if maos[x] == len(A) // 2:
                return x

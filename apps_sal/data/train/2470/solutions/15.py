class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import defaultdict
        counter = defaultdict(int)
        for domino in dominoes:
            counter[tuple(sorted(domino))] +=1
        return sum([v*(v-1)//2 for v in counter.values()])

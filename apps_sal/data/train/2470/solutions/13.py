class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        dicts = defaultdict(int)
        ans = 0

        for domi in dominoes:
            dicts[tuple(sorted(domi))] += 1

        for n in dicts.values():
            ans += n * (n - 1) // 2

        return ans

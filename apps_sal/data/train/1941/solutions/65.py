class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        cnt = Counter(frozenset(w) for w in words if len(set(w)) <= 7)
        ans = []
        for p in puzzles:
            cur = 0
            for k in range(7):
                for i in itertools.combinations(p[1:], k):
                    cur += cnt[frozenset((p[0],) + i)]
            ans.append(cur)
        return ans

from collections import Counter


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = Counter()
        for word in B:
            wordcnt = Counter(word)
            for c in wordcnt:
                if cnt[c] < wordcnt[c]:
                    cnt[c] = wordcnt[c]
        ans = []
        for word in A:
            wordcnt = Counter(word)
            if all((wordcnt[c] >= cnt[c] for c in cnt)):
                ans.append(word)
        return ans

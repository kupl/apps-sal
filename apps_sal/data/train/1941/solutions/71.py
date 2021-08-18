from functools import reduce


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        ans = [0] * len(puzzles)
        def T(): return collections.defaultdict(T)
        trie = T()
        for w in words:
            cur = reduce(dict.__getitem__, sorted(set(w)), trie)
            if '
                cur['
            else:
                cur['

        def dfs(cur, i, head):
            p = puzzles[i]
            if '
                ans[i] += cur['
            for c in cur:
                if c in p:
                    if p[0] == c or head:
                        dfs(cur[c], i, True)
                    else:
                        dfs(cur[c], i, False)
            return

        for i in range(len(puzzles)):
            dfs(trie, i, False)

        return ans

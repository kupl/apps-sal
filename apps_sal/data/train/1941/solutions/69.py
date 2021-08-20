class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = {}
        ans = [0] * len(puzzles)
        for word in words:
            cur = trie
            for w in sorted(set(word)):
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
            if '#' not in cur:
                cur['#'] = 1
            else:
                cur['#'] += 1

        def dfs(cur, i, head):
            p = puzzles[i]
            if '#' in cur and head:
                ans[i] += cur['#']
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

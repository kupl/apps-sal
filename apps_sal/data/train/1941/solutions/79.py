class Solution:

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        dic = {}
        for word in words:
            cur = dic
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            if '*' not in cur:
                cur['*'] = 1
            else:
                cur['*'] += 1
        res = [0 for _ in range(len(puzzles))]

        def dfs(i, dic, check_head):
            puzzle = puzzles[i]
            if '*' in dic and check_head:
                res[i] += dic['*']
            for k in dic:
                if k in puzzle:
                    if puzzle[0] == k or check_head:
                        dfs(i, dic[k], True)
                    else:
                        dfs(i, dic[k], False)
        for i in range(len(puzzles)):
            dfs(i, dic, False)
        return res

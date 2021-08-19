class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for f in folder:
            fo = f.split('/')
            curr = trie
            for letter in fo:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr['#'] = f

        def dfs(curr):
            if '#' in curr:
                res.append(curr['#'])
                return
            for key in curr:
                dfs(curr[key])
        res = []
        dfs(trie)
        return res

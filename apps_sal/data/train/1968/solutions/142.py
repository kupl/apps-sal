class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for f in folder:
            p = trie

            for c in f:
                if c not in p:
                    p[c] = {}
                p = p[c]
            if '/' not in p:
                p['/'] = {}
            p = p['/']
            p['$'] = f

        ans = []
        for f in folder:
            p = trie
            full = f + '/'
            for c in full:
                if '$' in p:
                    break
                p = p[c]
            else:
                ans.append(f)
        return ans

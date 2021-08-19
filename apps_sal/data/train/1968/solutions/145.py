class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = {}
        for f in folder:
            p = trie
            full = f + '/'
            for c in full:
                if c not in p:
                    p[c] = {}
                p = p[c]
            p['$'] = full
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

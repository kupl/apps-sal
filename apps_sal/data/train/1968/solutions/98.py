class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = dict()
        trie[''] = [0, dict()]
        for f in folder:
            curr = trie
            prev = None
            for c in f.split('/'):
                if c not in curr:
                    curr[c] = [0, dict()]
                prev = curr
                curr = curr[c][1]
            prev[c][0] = 1

        clean = []
        stack = [([''], trie[''])]
        while stack:
            p, (isPath, d) = stack.pop()
            if isPath == 0:
                for c in d:
                    stack.append((p + [c], d[c]))
            else:
                clean.append('/'.join(p))
        return clean

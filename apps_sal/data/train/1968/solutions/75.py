class TrieNode:
    def __init__(self):
        self.d = {}
        self.w = False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        root = TrieNode()
        res = []
        for file in folder:
            p = root
            end = False
            for w in file.split('/'):
                if p.w:
                    end = True
                    break
                if w not in p.d:
                    p.d[w] = TrieNode()
                p = p.d[w]
            if end:
                continue
            p.w = True
            res.append(file)
        return res

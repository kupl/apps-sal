class Trie:
    def __init__(self):
        self.chi = collections.defaultdict(Trie)
        self.ise = False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        sta = []
        for x in sorted(folder):
            node = root
            tmp = x[1:].split('/')
            for y in tmp:
                node = node.chi[y]
                if node.ise:
                    break
            else:
                node.ise = True
                sta.append(x)
        return sta

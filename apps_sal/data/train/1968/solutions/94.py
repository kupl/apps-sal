class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if folder is None or not folder:
            return []

        root = self._create_tree(folder)

        ret = []
        self._helper(root, [], ret)
        return ret

    def _helper(self, p, acc, ret):
        if p.is_word:
            ret.append('/' + '/'.join(acc))
            return

        for c in p.children:
            acc.append(c)

            self._helper(p.children[c], acc, ret)

            acc.pop()

    def _create_tree(self, folder):
        root = Node()

        for f in folder:
            t = f.split('/')
            p = root

            for i in range(1, len(t)):
                if p.is_word:
                    break

                name = t[i]
                if name not in p.children:
                    p.children[name] = Node()
                p = p.children[name]
            p.is_word = True
            p.children = {}

        return root

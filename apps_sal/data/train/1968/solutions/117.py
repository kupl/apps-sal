class TrieNode:
    def __init__(self):
        self.children = dict()
        self.path = None


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for directory in folder:
            curr = self.root
            for f in directory.split('/')[1:]:
                if f not in curr.children:
                    curr.children[f] = TrieNode()
                curr = curr.children[f]
            curr.path = directory

        def trie_search(node, res):
            if node.path:
                res.append(node.path)
                return res
            for nbr in node.children:
                res = trie_search(node.children[nbr], res)
            return res

        return trie_search(self.root, [])

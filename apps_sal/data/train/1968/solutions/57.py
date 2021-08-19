class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #
        class TrieNode:
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.index = -1
        res = []
        root = TrieNode()
        for i in range(len(folder)):
            trie = root
            for c in folder[i]:
                trie = trie.children[c]
            trie.index = i
        res = []

        # bfs
        q = [root]
        while q:
            node = q.pop(0)
            if node.index != -1:
                res.append(folder[node.index])
            # 文件名可能包含多个字符
            # [\"/a/b/c\",\"/a/b/ca\",\"/a/b/d\"]
            for c in node.children.keys():
                if node.index < 0 or c != '/':
                    q.append(node.children[c])

        return res

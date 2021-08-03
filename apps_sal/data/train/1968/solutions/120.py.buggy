class Node:
    def __init__(self):
        self.child = collections.defaultdict(Node)
        self.is_last = False
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.child[c]
        node.is_last = True
    def find(self):
        ret = []
        
        def dfs(node, tmp):
            if node.is_last:
                ret.append(\"/\".join(tmp))
                return
            for char, nxt_node in node.child.items():
                dfs(nxt_node, tmp+[char])
        dfs(self.root, [])
        return ret
        
    
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        t = Trie()
        for f in folder:
            t.insert(f.split(\"/\"))
        return t.find()

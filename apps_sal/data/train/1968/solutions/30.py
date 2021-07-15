class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, path):
        node = self.root
        for p in path:
            node = node.children[p]
        node.isEnd = True
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for f in folder:
            f = f.split(\"/\")[1:]
            self.add(f)
        
        ans = []
        self.dfs(self.root, [], ans)
        return ans
    
    def dfs(self, node, path, ans):
        if node.isEnd:
            ans.append(\"/\" + \"/\".join(path))
            return
        
        for c in node.children:
            self.dfs(node.children[c], path + [c], ans)
        
        

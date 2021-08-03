class TrieNode:
    def __init__(self, val):
        self.val = val
        self.next = {}
        self.path = None

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = TrieNode(\"\")
        
        for path in folder:
            node = trie
            names = path.split(\"/\")[1:]
            
            for name in names:
                if node.path:
                    break
                if name not in node.next:
                    node.next[name] = TrieNode(name)
                node = node.next[name]
            else:
                node.path = path
            
        res = []
        
        self.dfs(trie, res)
                
        return res
    
    def dfs(self, node, res):
        if node.path:
            res.append(node.path)
            return
        
        for child in node.next:
            self.dfs(node.next[child], res)
                    
# time: O(n*m)
# space: O(n*m)

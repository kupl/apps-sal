class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr_node = self.root
        
        for ch in word:
            if ch not in curr_node.children:
                curr_node.children[ch] = TrieNode()
            curr_node = curr_node.children[ch]
        curr_node.isEnd = True
    
    def find(self):
        def dfs(node, file, result):
            if node.isEnd:
                result.append(\"/\" + \"/\".join(file))
                return
            
            for ch in node.children:
                dfs(node.children[ch], file + [ch], result)
        result = []
        dfs(self.root, [], result)
        return result
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        
        for file in folder:
            file = file.split(\"/\")[1:]
            trie.insert(file)
        return trie.find()
        

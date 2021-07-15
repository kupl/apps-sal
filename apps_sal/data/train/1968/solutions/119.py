class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        t = Trie()
        
        for i in folder:
            t.insert(i.split(\"/\")[1:])
            
        return t.getFolders()
        
class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        for c in s:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.isEnd = True

    def getFolders(self):
        result = []
        
        def helper(node, path):
            if node.isEnd:
                result.append(path[:-1])
            else:
                for i in node.children:
                    helper(node.children[i],path + node.children[i].val + \"/\")

        helper(self.root, \"/\")
        
        return result

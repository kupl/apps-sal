class TrieNode:
    def __init__(self, name):
        self.children = {}
        self.isEnd = False
        self.name = name
        

class Trie:
    def __init__(self):
        self.root = TrieNode(\"\")
        
    def insert(self, word):
        it = self.root
        for w in word:
            if w not in it.children:
                it.children[w] = TrieNode(w)
                
            it = it.children[w]
        it.isEnd = True
    
    def normalize(self):
        self._normalize(self.root)
    
    def _normalize(self, node):
        if not node:
            return
        
        for char, childNode in node.children.items():
        
            hasSubFolders, child = self._normalize(childNode)
            if hasSubFolders and node.isEnd:
                node.children[child] = None

        return (node.isEnd, node.name)
        
    def getWords(self):
        lastWord = []
        result = []
        self._getWords(self.root, lastWord, result)
        return result
        
    def _getWords(self, node, lastWord, result):
        if not node:
            return
        
        if node.isEnd:
            result.append(\"/\".join(lastWord + [node.name]))
            return
        lastWord.append(node.name)
        for char, nodeChild in node.children.items():
            self._getWords(nodeChild, lastWord, result)
        lastWord.pop()
        


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for folder in folder:
            trie.insert(folder.split(\"/\")[1:])
            
        trie.normalize()
        
        return trie.getWords()
        

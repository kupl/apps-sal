class TrieTree:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.endWord = None
    
class Solution:
    ##这个文件夹可能不是只有一个单词的！！
    def __init__(self):
        self.root = TrieTree()
        
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for word in folder:
            wordList = word.split(\"/\")
            curr = self.root
            for letter in wordList:
                if letter not in curr.children:
                    curr.children[letter] = TrieTree()
                curr = curr.children[letter]
            curr.isEnd = True
            curr.endWord = word
            
        def dfs(root, path, result):
            if not root:
                return 
            
            if root.isEnd:
                result.append(root.endWord)
                return
            
            for i in root.children.keys():
                dfs(root.children[i], path + i, result)
            
        
        
        result = []
        dfs(self.root, \"\", result)
        return result
    
    

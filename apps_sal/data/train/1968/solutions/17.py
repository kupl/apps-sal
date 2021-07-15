class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode('$')
        self.answer = []
    
    def insert(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode(w)
            root = root.children[w]
        root.isWord = True
    
    def getCommonPrefix(self, root, prefix):
        if root.isWord:
            self.answer.append(prefix)  #If the current node is a folder end, then just get the prefix till here and ignore the further path.
            return
        
        children = root.children
        for c in children:
            self.getCommonPrefix(children[c], prefix+\"/\"+ children[c].val)
        
                
class Solution(object):
    def removeSubfolders(self, folders):
        \"\"\"
        :type folder: List[str]
        :rtype: List[str]
        \"\"\"
        trie = Trie()
        
        for f in folders:
            path = f.split(\"/\")
            path.pop(0)
            trie.insert(path)
        
        trie.getCommonPrefix(trie.root, \"\")
        
        return trie.answer
            
        
        
        
        
        
        
        
        
        # folder=sorted(folder)
        # ans=[]
        # for i in folder:
        #     flag=1
        #     for ele in ans:
        #         if(i.startswith(ele) and i[len(ele)]==\"/\"):
        #             flag=0
        #             break
        #     if(flag==1):
        #         ans.append(i)
        #     # print(ans)
        # return ans

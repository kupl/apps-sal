import collections
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isword = False
        
class trie:
    def __init__(self):
        self.res = TrieNode()
    def insert(self,word):
        cur = self.res
        for i in word:
            #rint(i)
            cur = cur.child[i]
        cur.isword=True
        
    def find(self):
        def dfs(node,stack,tmp):
            print(node.child.keys())
            if node.isword:
                stack.append(tmp)
                return 
            for item in node.child.keys():
                print(item)
                dfs(node.child[item],stack,tmp+\"/\"+item)
        stack =[]
        cur = self.res
        dfs(cur,stack,\"\")
        return stack
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res=trie()
        for item in folder:
            #print(item.split(\"/\")[1:])
            res.insert(item.split(\"/\")[1:])
        return res.find()

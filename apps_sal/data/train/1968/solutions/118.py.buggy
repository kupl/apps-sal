import collections
class Trienode:
    def __init__(self):
        self.child = collections.defaultdict(Trienode)
        self.isword = False
class trie:
    def __init__(self):
        self.res = Trienode()
    def insert(self,word):
        cur = self.res
        for i in word:
            cur = cur.child[i]
        cur.isword =True
    def find(self):
        self.stack =[]
        def dfs(node,tmp):
            for item in node.child.keys():
                if node.child[item].isword:
                    self.stack.extend([tmp+\"/\"+item])
                else:
                    dfs(node.child[item],tmp+\"/\"+item)
        dfs(self.res,\"\")
        return self.stack 
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        newres = trie()
        for item in folder:
            item = item.split(\"/\")[1:]
            newres.insert(item)
        
        return [item for item in newres.find()]

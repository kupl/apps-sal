class Node:
    def __init__(self):
        self.children = {}
        self.is_start = False

class StreamChecker:
    from collections import defaultdict
    
    
    def __init__(self, words: List[str]):
        self.queries = \"\"
        self.root = Node()
        self.found = False
        for word in words:
            r = self.root
            for ch in reversed(word):
                if r.children.get(ch,None):
                    r = r.children[ch]
                else:
                    n = Node()
                    r.children[ch] = n
                    r = n
            r.is_start = True
            
    def dfs(self):
        def dfs_util(node, str_):
            if not str_:
                return
            n = node.children.get(str_[0],None)
            if not n:
                return
            if n.is_start:
                self.found = True
            dfs_util(n, str_[1:])
            return
        dfs_util(self.root, self.queries)
            
            
        
        

    def query(self, letter: str) -> bool:
        self.queries = letter + self.queries
        #print(self.queries)
        self.found = False
        self.dfs()
        return self.found
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

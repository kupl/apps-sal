from collections import deque
class Node:
    def __init__(self):
        self.child = dict()
        self.end = False
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        
        for i in words:
            self.insert(self.root,i[::-1])
        self.key = deque()
        #print(self.root.child)
    def insert(self,root,key):
        for i in key:
            if root.child.get(i,None) == None:
                root.child[i] = Node()
            root = root.child[i]
        root.end = True
    def query(self, letter: str) -> bool:
        self.key.appendleft(letter)
        curr = self.root
        #print(self.key)
        for i in self.key:
            if curr.child.get(i,None) == None:break
            curr = curr.child[i]
            if curr.end:return True
        return False
            
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


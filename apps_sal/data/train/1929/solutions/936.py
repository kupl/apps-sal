class Node:
    def __init__(self, v=None):
        self.children: Dict[str, Node] = {}
        self.parent: Node
        self.value = v
    
class Trie:
    def __init__(self):
        self.t = Node() #root;
        self.leaves: Dict[str, List[Node]] = {}
        self.maxLen: int = 0

    def addLeave(self, w:str, n:Node) -> None:
        if w not in list(self.leaves.keys()):
            self.leaves[w] = []
        self.leaves[w].append(n)
        
    def insert(self, w: str) -> None:
        self.maxLen = max(self.maxLen, len(w))
        tl = self.t
        j = 0
        while j<len(w):
            i = w[j]
            n = tl.children.get(i, None)
            if n != None: #this char exist
                tl = n
                j += 1
            else:
                for i in w[j:]:
                    newNode = Node(i)
                    newNode.parent = tl
                    tl.children[i] = newNode
                    tl = newNode
                break
        self.addLeave(tl.value, tl)


class StreamChecker:
    from collections import deque
    
    def __init__(self, words: List[str]):
        self.trie = Trie()
        [self.trie.insert(w) for w in words]
        self.q = deque(maxlen = self.trie.maxLen)
                
    def query(self, letter: str) -> bool:
        self.q.append(letter)
        fl = self.trie.leaves.get(letter, None)
        if fl==None:
            return False
        
        for f in fl:
            i = len(self.q) -2
            if f.parent.value==None: #reached root
                return True #already reach
            while i>=0:
                l = self.q[i]
                if f.parent.value == l:
                    f = f.parent
                    i -= 1
                else:
                    break
                
                if f.parent.value==None: #reached root
                    return True #already reach

        return False
                
            
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


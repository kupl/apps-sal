class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        curr = self.root
        for c in word:
            if curr.has(c):
                curr = curr.child(c)
            else:
                curr.add(c)
                curr = curr.child(c)
        curr.end()
        
    def search(self, word):
        curr = self.root
        for c in word:
            if curr.terminal:
                return True
            elif not curr.has(c):
                return False
            else:
                curr = curr.child(c)
        return curr.terminal
        
    def display(self):
        def recurse(node, pref):
            print (''.join(pref), node.terminal)
            for letter, child in node.children.items():
                recurse(child, pref + [letter])
        
        pref = []
        recurse(self.root, pref)
        
class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False
        
    def end(self):
        self.terminal = True
    
    def has(self, c):
        return c in self.children
    
    def add(self, c):
        self.children[c] = Node()
    
    def child(self, c):
        return self.children[c]
    
    def __str__(self):
        return \"nd\"
    
    def __repr__(self):
        return \"nd\"
    

def rev(L):
    # reverse iterator
    for i in range(len(L) - 1, -1, -1):
        yield L[i]
    
class StreamChecker:
    def __init__(self, words: List[str]):
        # Set trie up for reverses of words
        # always search in reverse
        self.T = Trie()
        for word in words:
            self.T.add(rev(word))
        self.stream = []
        self.T.display()
        
        
    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        return self.T.search(rev(self.stream))

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

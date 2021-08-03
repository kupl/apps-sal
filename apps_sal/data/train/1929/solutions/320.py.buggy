class Node:

    def __init__(self):
        self.edges = {}
        
    def hasEdge(self, edge):
        return edge in self.edges
    
    def getEdge(self, edge):
        return self.edges[edge]
    
    def addEdge(self, edge):
        if not self.hasEdge(edge):
            self.edges[edge] = Node()
    
    def isEnd(self):
        return \"*\" in self.edges
    
class Trie:
    
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        node = self.root
        
        for c in word:
            if not node.hasEdge(c):
                node.addEdge(c)   
            node = node.getEdge(c)
            
        node.addEdge(\"*\")
        
    def search(self, stream):
        node = self.root
        
        for c in stream:
            if not node.hasEdge(c):
                return False
            
            node = node.getEdge(c)
            
            if node.hasEdge(\"*\"):
                return True
        
        return False
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = collections.deque()
        
        for word in words:
            self.trie.addWord(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.search(self.stream)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)



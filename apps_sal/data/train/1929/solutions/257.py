class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isStart = False
        
        
class Trie:
    def __init__(self, words: List[str]):
        self.root = Node()
        self.maxLen = 0
        
        for word in words:
            self.maxLen = max(self.maxLen, self.insert(word))
            
    def insert(self, word: str) -> int:
        i = 0
        current = self.root
        for char in word[::-1]:
            current = current.children[char]
            i += 1
            
        current.isStart = True
        return i
    
    def endsWith(self, word: str) -> bool:
        current = self.root
        for char in word:
            if current.isStart:
                return True
            if char not in current.children:
                return False
            current = current.children[char]
            
        return current.isStart
        
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.wl = Trie(words)
        self.bufSize = self.wl.maxLen
        self.history = collections.deque()

    def query(self, letter: str) -> bool:
        self.history.appendleft(letter)
        if len(self.history) > self.bufSize:
            self.history.pop()  
            
        return self.wl.endsWith(''.join(self.history))


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class Node:
    def __init__(self, val=None):
        self.kids = defaultdict(Node)
        self.val = val
        self.word = False
        
class Trie:
    def __init__(self):
        self.head = Node()
        
    def add(self, word):
        N = len(word)
        curr = self.head
        
        for i in range(N-1, -1, -1):
            c = word[i]
            curr = curr.kids[c]
            
        curr.word = True
    
        
    def search(self, word):
        N = len(word)
        curr = self.head
        
        for i in range(N-1, -1, -1):
            c = word[i]
            if c in curr.kids:
                curr = curr.kids[c]
                if curr.word:
                    return True
            else:
                return False
            
        return curr.word
    
    
            
            
        
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.max = 0
        
        for word in words:
            self.trie.add(word)
            self.max = max(self.max, len(word))
        
        self.history = deque()

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        if len(self.history) > self.max:
            self.history.popleft()
            
        out = self.trie.search(self.history)
        print(letter, \"->\", out)
        return out
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_end = False
        
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.last_k = collections.deque()
        self.k = max(len(word) for word in words)
        
        for word in words:
            self._insert(word[::-1])
            
    def _insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.child[ch]
        curr.is_end = True        

    def query(self, letter: str) -> bool:
        self.last_k.appendleft(letter)      
        if len(self.last_k) > self.k:   # maintain a window size of k
            self.last_k.pop()
        
        curr = self.root
        for ch in self.last_k:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
            if curr.is_end:
                return True
        return curr.is_end
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


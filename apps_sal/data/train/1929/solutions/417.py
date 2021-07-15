class TrieNode:
    def __init__(self):
        self.data = collections.defaultdict(TrieNode)
        self.isWord = False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.rec = collections.defaultdict(set)
        self.maxsize = float('-inf')
        self.minsize = float('inf')
        self.root = TrieNode()
        for w in words:
            self.maxsize = max(len(w), self.maxsize)
            self.minsize = min(len(w), self.minsize)
            curr = self.root
            for c in w[::-1]:
                curr = curr.data[c]
            
            curr.isWord = True

        self.curr = \"\"

    def query(self, letter: str) -> bool:
        
        self.curr += letter        
        #self.curr = self.curr[-self.maxsize:]
        
        curr = self.root
        for c in self.curr[::-1]:
            if c in curr.data:
                curr = curr.data[c]
                if curr.isWord:
                    return True
            else:
                return False
            
        return False
            
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

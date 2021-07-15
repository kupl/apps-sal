class node:
    def __init__(self):
        self.isword = False
        self.child = defaultdict(node)
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.history = \"\"
        self.root = node()
        
        for w in words:
            cur = self.root
            for c in w[::-1]:
                cur = cur.child[c]
            cur.isword = True
        

    def query(self, letter: str) -> bool:
        cur = self.root
        self.history += letter
        for c in self.history[::-1]:
            if c not in cur.child: return False
            cur = cur.child[c]
            if cur.isword: return True
            
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

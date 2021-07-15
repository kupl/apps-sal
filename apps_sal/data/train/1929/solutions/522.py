class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)
        
class StreamChecker:

    def __init__(self, words: List[str]):
        if not words: return False
        self.root = TrieNode()
        for word in words:
            self.addNode(word[::-1])
        self.buff = []
        self.maxl = len(max(words, key = lambda x: len(x)))
        

    def query(self, letter: str) -> bool:
        self.buff.append(letter)
        s = \"\"
        for i in range(len(self.buff) - 1, -1, -1):
            s += self.buff[i]
            if len(s) > self.maxl: 
                break
            print(s)
            res = self.findWord(s)
            if not res: return False
            if res.is_word: return True
        return False
            
        
    def addNode(self, word):
        p = self.root
        for w in word:
            if not p.children.get(w):
                p.children[w] = TrieNode()
            p = p.children[w]
        p.is_word = True
    
    def findWord(self,word):
        p = self.root
        for w in word:
            if not p.children.get(w):
                return False
            p = p.children[w]
            
        return p

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

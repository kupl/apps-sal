class TrieNode():
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.res = []
        for word in words:
            self.add(word)
        

    def query(self, letter: str) -> bool:
        curr = self.root
        self.res.insert(0,letter)
        for char in self.res:
            if curr.isWord:
                return True
            if not curr.child.get(char):
                return False
            curr = curr.child[char]
        return curr.isWord
    
    def add(self,word):
        curr = self.root
        for char in word[::-1]:
            curr = curr.child[char]
        curr.isWord = True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


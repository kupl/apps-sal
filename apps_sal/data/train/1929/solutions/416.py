class TrieNode:
    def __init__(self):
        self.dict = defaultdict(TrieNode)
        self.word = False
        
class StreamChecker:
    

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.prefix = ''
        
        for word in words:
            node = self.root
            
            for char in word[::-1]:
                node = node.dict[char]
            
            node.word = True

    def query(self, letter: str) -> bool:
        self.prefix += letter
        node = self.root
        
        for char in self.prefix[::-1]:
            if char not in node.dict:
                break
            
            node = node.dict[char]
            
            if node.word == True:
                return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


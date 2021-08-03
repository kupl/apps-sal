class Trie:
    def __init__(self):
        self.word = \"\"
        self.kids = dict()
        
class StreamChecker:
    
    
    def __init__(self, words: List[str]):
        self.root = Trie()
        def add(word):
            node = self.root
            for ch in word:
                if not node.kids.get(ch, None):
                    node.kids[ch] = Trie()
                node = node.kids[ch]
            node.word = word
        for word in words:
            add(word[::-1])
        self.stream = []
            

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.root
        for i in range(len(self.stream)-1, -1, -1):
            ch = self.stream[i]
            if not node.kids.get(ch, None):
                return False
            node = node.kids.get(ch)
            if node.word:
                return True
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

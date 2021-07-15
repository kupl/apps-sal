class Trie:
    def __init__(self):
        self.child = {}
        self.isEnd = False
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.str = []
        
        for word in words:
            node = self.root
            for ch in reversed(word) :
                if ch not in node.child:
                    node.child[ch] = Trie()
                node = node.child[ch]
            node.isEnd = True
    def query(self, letter: str) -> bool:
        self.str.insert(0, letter)
        
        node = self.root
        for ch in self.str:
            if ch not in node.child:
                return False
            node = node.child[ch]
            if node.isEnd:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class TrieNode():
    def __init__(self):
        self.children = {}
        self.isend = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode()) # setdefault(key, default=None)
        root.isend = 1


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        
        self.stream = deque()
        
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        cur = self.trie.root
        for c in self.stream:
            if c in cur.children:
                cur = cur.children[c]
                if cur.isend: return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


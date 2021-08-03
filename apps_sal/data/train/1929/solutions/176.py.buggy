from collections import deque
class Trie:
    def __init__(self, words):
        self.root = {}
        self.build(words)
    
    def build(self, words):
        for word in words:
            self.add_word(word[::-1])
            
    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[\"$\"] = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie(words)
        self.prev_letters = deque([])

    def query(self, letter: str) -> bool:
        self.prev_letters.appendleft(letter)
        node = self.trie.root
        for ch in self.prev_letters:
            if \"$\" in node:
                return True
            if ch in node:
                node = node[ch]
            else:
                return False
        
        return \"$\" in node

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
\"\"\"
a, b, c, d

abcd, bcd, cd, d

\"\"\"

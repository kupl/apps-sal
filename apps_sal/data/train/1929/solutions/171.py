class Trie:
    def __init__(self):
        self.child = {}

    def insert(self, word):
        cur = self
        for char in word + '$':
            if char not in cur.child:
                cur.child[char] = Trie()
            cur = cur.child[char]

    def search(self, word):
        cur = self
        for char in word + '$':
            if '$' in cur.child: return True
            if char in cur.child:
                cur = cur.child[char]
            else:
                return False
        return False
#
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            word = word[::-1]
            self.trie.insert(word)
        self.buffer = ''
    

    def query(self, letter: str) -> bool:
        self.buffer=letter+ self.buffer
        return self.trie.search(self.buffer)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class Trie:
    def __init__(self):
        self.child = {}

    def insert(self, word):
        cur_trie = self
        for char in word + '$':  # using $ to indicate end of word
            if char not in cur_trie.child:
                cur_trie.child[char] = Trie()
            cur_trie = cur_trie.child[char]

    def search(self, word):
        cur_trie = self
        for char in word + '$':
            if '$' in cur_trie.child: return True
            if char not in cur_trie.child: return False
            
            cur_trie = cur_trie.child[char]

        return False


class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.buffer = ''

    def query(self, letter: str) -> bool:
        self.buffer = letter + self.buffer
        return self.trie.search(self.buffer) 


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


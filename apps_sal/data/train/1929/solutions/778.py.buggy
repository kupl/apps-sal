class Trie:

    def __init__(self, val=''):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.val = val
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        node = self
        i = 0
        while i < len(word) and word[i] in node.children:
            node = node.children[word[i]]
            i += 1
        for j in range(i, len(word)):
            node.children[word[j]] = Trie(word[j])
            node = node.children[word[j]]
        node.is_end = True

    def search(self, word: str) -> bool:
        \"\"\"
        Returns if the word is in the trie.
        \"\"\"
        node = self
        for lett in word:
            if lett not in node.children:
                return False
            node = node.children[lett]
        return node.is_end
    
    def cutIfStartsWith(self, prefix: str) -> bool:
        \"\"\"
        Returns if there is any word in the trie that starts with the given prefix.
        \"\"\"
        node = self
        for lett in prefix:
            if lett not in node.children:
                return False
            node = node.children[lett]
        node.children = {}
        node.is_end = True
        return True

class StreamChecker:

    def __init__(self, words: List[str]):
        btrie = Trie()
        for w in words:
            bw = w[::-1]
            if not btrie.cutIfStartsWith(bw):
                btrie.insert(bw)
        def get_words(trie):
            return [''] if trie.is_end else [tail + c for c in trie.children for tail in get_words(trie.children[c])]
        self.trie = Trie()
        for w in get_words(btrie):
            self.trie.insert(w)
        self.cur = set()
        

    def query(self, letter: str) -> bool:
        self.cur.add(self.trie)
        self.cur = {t.children[letter] for t in self.cur if letter in t.children}
        for t in self.cur:
            if t.is_end:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add_word(word)
            
        self.candidates = [self.trie.root]

    def query(self, letter: str) -> bool:
        new_candidates = [self.trie.root]
        ans = False
        for option in self.candidates:
            if letter in option.children:
                child = option.children[letter]
                new_candidates.append(child)
                ans = ans or child.is_word
        self.candidates = new_candidates
        return ans


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


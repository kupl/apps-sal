class TrieNode:
    def __init__(self):
        self.letters = {}
        self.word = False

    def trie(self, words):
        root = TrieNode()
        for word in words:
            current = root
            for letter in word:
                if letter not in current.letters:
                    current.letters[letter] = TrieNode()
                current = current.letters[letter]
            current.word = True
        return root


class StreamChecker:

    def __init__(self, words: List[str]):
        trie = TrieNode()
        self.root = trie.trie(words)
        self.left = [self.root]

    def query(self, letter: str) -> bool:
        right = [self.root]
        finded = False
        for trie in self.left:
            if letter in trie.letters:
                tmp = trie.letters[letter]
                right += [tmp]
                if tmp.word:
                    finded = True
        self.left = right
        return finded


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

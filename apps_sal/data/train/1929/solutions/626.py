class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def find_any(self, word):
        node = self.root
        for c in word:
            if node.is_word:
                return True
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add_word(word[::-1])
        self.cur = ''

    def query(self, letter: str) -> bool:
        self.cur += letter
        return self.trie.find_any(self.cur[::-1])

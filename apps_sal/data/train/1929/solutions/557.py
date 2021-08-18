class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie([word[::-1] for word in words])
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.insert(0, letter)
        curr = self.trie.head
        i = 0
        while curr and i < len(self.stream):
            curr = curr.get_element(self.stream[i])
            if not curr:
                return False
            if curr.is_word:
                return True
            i += 1


class TrieNode:
    ORDA = ord('a')

    def __init__(self, is_word: bool = False):
        self.is_word = is_word
        self.children = [None] * 26

    def get_element(self, c: str):
        idx = ord(c) - TrieNode.ORDA
        return self.children[idx]

    def ensure_element(self, c: str):
        idx = ord(c) - TrieNode.ORDA
        if not self.children[idx]:
            self.children[idx] = TrieNode()
        return self.children[idx]


class Trie:
    def __init__(self, words: List[str]):
        self.head = TrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word: str):
        curr = self.head
        for c in word:
            curr = curr.ensure_element(c)
        curr.is_word = True

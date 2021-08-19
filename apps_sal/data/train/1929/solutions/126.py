from collections import defaultdict
from collections import deque


class TrieNode:
    def __init__(self):
        self.is_word = False  # flag for complete word
        self.children = defaultdict(TrieNode)  # dictionary to store children TrieNodes


class Trie:
    def __init__(self, words=None):
        self.root = TrieNode()
        if words:
            for word in words:
                self.insert(word)

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]

        curr.is_word = True

    def search(self, word):
        curr = self.root
        for char in word:
            if curr.children.get(char, None) is None:
                return False
            curr = curr.children[char]
        return curr.is_word

    def starts_with(self, prefix):
        # prefix can be a string as well as a list of chars
        curr = self.root
        for char in prefix:
            if curr.children.get(char, None) is None:
                return False
            curr = curr.children[char]
        return True

    def contains_stream(self, stream, index=0):
        # stream can be a string as well as a list of chars
        curr = self.root
        while index < len(stream):
            if curr.is_word:
                return True
            char = stream[index]
            if curr.children.get(char, None) is None:
                return False
            curr = curr.children[char]
            index += 1
        return curr.is_word


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        # add words in reverse
        for word in words:
            self.trie.insert(word[::-1])

        # for word in words:
        #     print(self.trie.search(word[::-1]))

        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.contains_stream(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

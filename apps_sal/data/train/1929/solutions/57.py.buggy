from collections import deque
class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = Node(\"\")

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.word = True

    def prefix_of_word_exists(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.word:
                return True
        return False
        

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.max_word_length = 0
        for word in words:
            self.trie.add_word(word[::-1])
            self.max_word_length = max(self.max_word_length, len(word))
        self.q = deque()

    def query(self, letter: str) -> bool:
        if len(self.q) == self.max_word_length:
            self.q.pop()
        self.q.appendleft(letter)
        return self.trie.prefix_of_word_exists(self.q)
    # [\"cde\"]
    # [\"c\" Node<d>, \"d\" None] e
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

from typing import Dict


class Node:
    def __init__(self, char=None):
        self.char = char
        self.is_complete_word = False
        self.children: Dict[str, 'Node'] = dict()


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.is_complete_word = True


class StreamChecker:
    def __init__(self, words: List[str]):
        self.waitlist = []
        self._max_length = 0
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
            self._max_length = max(self._max_length, len(word))

    def query(self, letter: str) -> bool:
        self.waitlist.append(letter)
        i = len(self.waitlist) - 1
        node = self.trie.root
        while i >= 0:
            if node.is_complete_word:
                return True
            letter = self.waitlist[i]
            if letter not in node.children:
                return False
            node = node.children[letter]
            i -= 1
        return node.is_complete_word

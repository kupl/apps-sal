from typing import List

root = '@'
marker = '$'


class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()


class StreamChecker:

    def __init__(self, words: List[str]):
        self.spelt = False
        self.root = TrieNode(root)
        self.pointers = [self.root]

        for word in words:
            self.trie_insert(word)

    def trie_insert(self, word: str):
        current = self.root

        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                letter_node = TrieNode(letter)
                current.children[letter] = letter_node
                current = letter_node
        current.children[marker] = TrieNode(marker)

    def query(self, letter: str) -> bool:
        new_ptrs = []
        self.spelt = False
        for ptr in self.pointers:
            if letter in ptr.children:
                advanced_ptr = ptr.children[letter]
                if marker in advanced_ptr.children:
                    self.spelt = True
                new_ptrs.append(advanced_ptr)
                
        self.pointers = new_ptrs + [self.root]
        return self.spelt



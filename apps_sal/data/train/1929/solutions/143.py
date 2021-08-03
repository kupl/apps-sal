'''
Approach 1:
* Have a dict mapping letters to words ending on that letter.
* Have a list with all the letters queried so far.
* In query(), add letter to the list.
* For each word ending on the queried letter, check if the other letters have been queried as well.

Approach 2:
* Have a trie with words in 'words'.
* Have a list with all letters queried so far.
* Traverse the trie using the letters in the list (scanning backwards).
'''

from collections import defaultdict


class TrieNode:

    def __init__(self):
        self.links = dict()
        self.is_word = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie_root = build_trie(words)
        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.append(letter)

        index = -1
        node = self.trie_root
        while node.links:
            if index < -len(self.queries):
                break
            letter = self.queries[index]
            if letter not in node.links:
                break
            index -= 1
            node = node.links[letter]
            if node.is_word:
                return True
        return False


def build_trie(words):
    root = TrieNode()
    for word in words:
        insert(root, word)
    return root


def insert(root, word):
    node = root
    for char in reversed(word):
        if char not in node.links:
            node.links[char] = TrieNode()
        node = node.links[char]
    node.is_word = True

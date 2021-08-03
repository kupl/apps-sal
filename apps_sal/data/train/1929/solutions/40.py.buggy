from collections import defaultdict
from typing import List, Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_terminal: bool = False

    def __repr__(self):
        return f\"<terminal = {self.is_terminal}, children = {self.children}>\"

class StreamChecker:

    def __init__(self, words: List[str]):
        self._starts_with: Dict[str, List[str]] = defaultdict(list)
        unique_words = set(words)
        self._trie = TrieNode()
        for word in unique_words:
            self._add_to_trie(word)
        #print(self._trie)

        self._pointers: List[TrieNode] = []


    def _add_to_trie(self, word: str):
        trie_node = self._trie
        for i, c in enumerate(word):
            if c not in trie_node.children:
                trie_node.children[c] = TrieNode()
            trie_node = trie_node.children[c]
            if i == len(word) - 1:
                trie_node.is_terminal = True


    def query(self, letter: str) -> bool:
        #print(letter)
        #print(f\"Starting out with {self._pointers}\")
        # Advance pointers currently active
        advancing_pointers = []
        found = False

        for trie_node in self._pointers:
            new_node = trie_node.children.get(letter)
            if new_node is not None:
                if new_node.is_terminal:
                    found = True
                advancing_pointers.append(new_node)

        from_root = self._trie.children.get(letter)
        if from_root is not None:
            if from_root.is_terminal:
                found = True
            advancing_pointers.append(from_root)

        self._pointers = advancing_pointers
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

from collections import defaultdict
import queue


class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.cstream = []
        for word in words:
            curr = self.root
            for c in word[::-1]:
                curr = curr.children[c]
            curr = curr.children['$']

    def query(self, letter: str) -> bool:
        self.cstream.insert(0, letter)
        curr = self.root
        for c in self.cstream:
            if '$' in curr.children:
                return True
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return '$' in curr.children
        pass

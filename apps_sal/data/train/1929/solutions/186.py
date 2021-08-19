from collections import deque, defaultdict as dd


class TrieNode:

    def __init__(self):
        self.children = dd(TrieNode)
        self.is_end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.q = deque()
        self.root = TrieNode()
        for word in words:
            node = self.root
            for char in word[::-1]:
                node = node.children[char]
            node.is_end = True

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        node = self.root
        for char in self.q:
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_end:
                return True
        return False

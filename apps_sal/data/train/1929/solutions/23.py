from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.processing = []
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.end = True

    def search(self, c):
        processed = []
        self.processing.append(self.root)
        found = False
        for node in self.processing:
            if c in node.children:
                node = node.children[c]
                processed.append(node)
                found |= node.end

        self.processing = processed
        return found


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie(words)

    def query(self, letter: str) -> bool:
        return self.trie.search(letter)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

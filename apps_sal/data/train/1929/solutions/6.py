class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word)

    def query(self, char: str) -> bool:
        return self.trie.find(char)


class Trie:

    class Node:

        def __init__(self, complete=False):
            self.complete = complete
            self.children = {}

    def __init__(self):
        self.root = self.Node()
        self.current = []

    def add(self, word: str) -> bool:
        node = self.root
        for (index, char) in enumerate(word):
            if char not in node.children:
                node.children[char] = self.Node(index == len(word) - 1)
            node = node.children[char]
            if index == len(word) - 1:
                node.complete = index == len(word) - 1
        return True

    def find(self, char: str) -> bool:
        self.current.append(self.root)
        self.current = [node.children[char] for node in self.current if char in node.children]
        return any((node.complete for node in self.current))

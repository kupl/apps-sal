class Node:

    def __init__(self, end=False):
        self.end = end
        self.children = [None] * 26

    def search(self, word):
        curr = self
        for w in word:
            slot = ord(w) - ord('a')
            if curr.children[slot]:
                curr = curr.children[slot]
                if curr.end:
                    return True
            else:
                return False
        return curr.end


class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = ''
        self.root = Node('')

        def add(node, word):
            for w in word:
                slot = ord(w) - ord('a')
                if node.children[slot] is None:
                    node.children[slot] = Node()
                node = node.children[slot]
            node.end = True
        for word in words:
            add(self.root, word[::-1])

    def query(self, letter: str) -> bool:
        self.letters = letter + self.letters
        return self.root.search(self.letters)

class TrieNode:

    def __init__(self):
        self.children = {}
        self.terminal = False


class StreamChecker:

    def __init__(self, words: List[str]):

        def addword(word):
            node = self.root
            for char in reversed(word):
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.terminal = True
        self.array = []
        self.root = TrieNode()
        for word in words:
            addword(word)

    def query(self, letter: str) -> bool:
        array = self.array
        node = self.root
        array.append(letter)
        for char in reversed(array):
            if char in node.children:
                node = node.children[char]
                if node.terminal:
                    return True
            else:
                return False

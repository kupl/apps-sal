class StreamChecker:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.endOfWord = False

    def __init__(self, words: List[str]):
        self.root = self.TrieNode()
        self.stream = []

        for word in words:
            node = self.root
            for char in word[::-1]:
                if char not in node.children:
                    node.children[char] = self.TrieNode()
                node = node.children[char]
            node.endOfWord = True

    def query(self, letter: str) -> bool:
        node = self.root
        self.stream.insert(0, letter)
        for char in self.stream:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.endOfWord == True:
                return True
                break

        return False

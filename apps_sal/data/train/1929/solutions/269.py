class Trie:
    def __init__(self):
        self.node = TrieNode()

    def add(self, wordadd):
        node = self.node
        for char in wordadd:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.isEnd = True


class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.letters = []
        self.rootNode = Trie()
        for word in words:
            self.rootNode.add(word[::-1])

    def query(self, letter: str) -> bool:
        self.letters.insert(0, letter)
        node = self.rootNode.node
        for letter in self.letters:
            if node.isEnd:
                return True
            if letter not in node.child:
                return False
            node = node.child[letter]
        return node.isEnd

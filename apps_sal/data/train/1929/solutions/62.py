class TrieNode:
    def __init__(self):
        self.neighbors = defaultdict(TrieNode)
        self.isWord = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            node = self.root
            for c in word:
                node = node.neighbors[c]
            node.isWord = True
        self.nodes = []

    def query(self, letter: str) -> bool:
        isWord = False
        newNodes = []
        self.nodes.append(self.root)
        for node in self.nodes:
            if letter in node.neighbors:
                temp = node.neighbors[letter]
                isWord |= temp.isWord
                newNodes.append(temp)
        self.nodes = newNodes
        return isWord

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


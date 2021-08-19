class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.waiting = []
        for word in words:
            self.root.insert(word)

    def query(self, letter: str) -> bool:

        self.waiting = [node.child[letter] for node in self.waiting + [self.root] if letter in node.child]

        for node in self.waiting:
            if node.is_complete:
                return True

        return False


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_complete = False

    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.child:
                new_node = TrieNode()
                node.child[letter] = new_node
            node = node.child[letter]
        node.is_complete = True


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

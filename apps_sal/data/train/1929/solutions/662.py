class TreeNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TreeNode()
        self.sofar = ''
        for word in words:
            self.add(word)

    def add(self, word):
        node = self.root
        for w in word[::-1]:
            if w not in node.children:
                node.children[w] = TreeNode()
            node = node.children[w]
        node.isWord = True

    def query(self, letter: str) -> bool:
        self.sofar += letter
        node = self.root
        for c in self.sofar[::-1]:
            if c in node.children:
                node = node.children[c]
                if node.isWord:
                    return True
            else:
                return False
        return node.isWord


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

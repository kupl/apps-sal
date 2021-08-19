class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.q = ''
        self.root = TrieNode()
        for word in words:
            root = self.root
            for w in word[::-1]:
                root = root.children.setdefault(w, TrieNode())
            root.isEnd = True

    def dfs(self, node, n) -> bool:
        # n: pos back from self.q
        if n > len(self.q):
            return False
        if self.q[-n] in node.children:
            if node.children[self.q[-n]].isEnd:
                return True
            else:
                return self.dfs(node.children[self.q[-n]], n + 1)
        else:
            return False

    def query(self, letter: str) -> bool:
        self.q += letter
        return self.dfs(self.root, 1)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

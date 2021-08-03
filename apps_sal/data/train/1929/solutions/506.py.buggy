class Node:
    def __init__(self):
        self.kids = collections.defaultdict(Node)
        self.end = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        self.s = \"\"
        for word in words:
            t = self.root
            for w in word[::-1]:
                t = t.kids[w]
            t.end = True

    def query(self, letter: str) -> bool:
        self.s += letter
        def dfs(t, word):
            for w in word:
                if w not in t.kids:
                    return False
                t = t.kids[w]
                if t.end:
                    return True
            return False
        return dfs(self.root, self.s[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

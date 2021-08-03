class StreamChecker:

    class Node:
        def __init__(self):
            self.node = [None] * 26
            self.end = False

    def __init__(self, words: List[str]):
        self.s = ''
        self.root = self.Node()
        for word in words:
            node = self.root
            n = len(word)
            word = word[::-1]
            for i in range(n):
                a = ord(word[i]) - ord('a')
                if not node.node[a]:
                    node.node[a] = self.Node()
                if i == n - 1:
                    node.node[a].end = True
                else:
                    node = node.node[a]
            print((node.node, node.end))

    def query(self, letter: str) -> bool:
        self.s = letter + self.s
        node = self.root
        for i in self.s:
            a = ord(i) - ord('a')
            if not node.node[a]:
                return False
            if node.node[a].end:
                print((not node.node[a]))
                return True
            node = node.node[a]
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

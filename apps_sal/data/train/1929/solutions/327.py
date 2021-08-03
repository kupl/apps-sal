class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = self.getNode()
        for word in words:
            self.addWord(word[::-1])
        self.currStr = deque([])

    def addWord(self, word):
        node = self.root
        for c in word:
            ind = self.getInd(c)
            if node.children[ind] == None:
                node.children[ind] = self.getNode()
            node = node.children[ind]
        node.isEnd = True

    def getInd(self, c):
        return ord(c) - ord('a')

    def getNode(self):
        return TrieNode()

    def findWord(self, letter):
        self.currStr.appendleft(letter)

        node = self.root
        for ch in self.currStr:
            ind = self.getInd(ch)
            if node.children[ind] == None:
                return False
            elif node.children[ind].isEnd:
                return True
            node = node.children[ind]

        return node and node.isEnd

    def query(self, letter: str) -> bool:
        return self.findWord(letter)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

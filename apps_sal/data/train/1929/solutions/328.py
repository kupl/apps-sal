
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = self.getNode()
        self.currStr = deque([])
        for word in words:
            self.addWord(word[::-1])

    def getNode(self):
        return TrieNode()

    def getInd(self, c):
        return ord(c) - ord('a')

    def addWord(self, word):
        node = self.root
        for ch in word:
            ind = self.getInd(ch)
            if node.children[ind] == None:
                node.children[ind] = self.getNode()
            node = node.children[ind]
        node.isEnd = True

    def query(self, letter: str) -> bool:
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

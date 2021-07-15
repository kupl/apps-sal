class TrieNode:

    def __init__(self):
        self.dic = defaultdict(TrieNode)
        self.isWord = False

    def addWord(self, word):
        node = self
        for char in word:
            if not node.dic[char]:
                node.dic[char] = TrieNode()
            node = node.dic[char]
        node.isWord = True


class StreamChecker:

    def __init__(self, words):
        self.root = TrieNode()
        self.stream = \"\"
        for word in words:
            self.root.addWord(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream += letter
        node = self.root
        i = len(self.stream) - 1
        while i >= 0 and self.stream[i] in node.dic:
            node = node.dic[self.stream[i]]
            if node.isWord:
                return True
            i -= 1
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

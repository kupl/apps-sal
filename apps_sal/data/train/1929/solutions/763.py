class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addNode(self, word):
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            curNode = curNode.children[char]
        curNode.isEnd = True

    def search(self, word):
        curNode = self.root
        for char in word:

            if char not in curNode.children:
                return False
            else:
                curNode = curNode.children[char]
                if curNode.isEnd:
                    return True
                else:
                    pass
        return curNode.isEnd


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.addNode(word[::-1])
        self.curWord = ''

    def query(self, letter: str) -> bool:
        self.curWord = letter + self.curWord
        return self.trie.search(self.curWord)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

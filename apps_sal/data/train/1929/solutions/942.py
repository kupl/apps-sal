class Node:
    def __init__(self, val='', endWord=False):
        self.val = val
        self.endWord = endWord
        self.children = dict()


class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            self.insertWord(word)

    def insertWord(self, word):
        currentNode = self.root
        for letter in word:
            if not letter in currentNode.children:
                currentNode.children[letter] = Node(letter)
            currentNode = currentNode.children[letter]
        currentNode.endWord = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie(words)
        self.trieRoot = self.trie.root
        self.currentNodes = []

    def query(self, letter: str) -> bool:
        newNodes = []
        if letter in self.trieRoot.children:
            newNodes.append(self.trieRoot.children[letter])

        for node in self.currentNodes:
            if letter in node.children:
                newNodes.append(node.children[letter])

        self.currentNodes = newNodes
        for node in self.currentNodes:
            if node.endWord:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.links = {}
        self.is_end = False

    def getLink(self, char):
        return self.links.get(char)

    def addLink(self, node):
        self.links[node.val] = node

    def setEnd(self):
        self.is_end = True


class Trie:
    def __init__(self):
        self.roots = [None] * 26

    def insertWord(self, word):
        if self.roots[ord(word[0]) - ord('a')] is None:
            self.roots[ord(word[0]) - ord('a')] = TrieNode(word[0])

        currNode = self.roots[ord(word[0]) - ord('a')]

        for i in range(1, len(word)):
            char = word[i]
            nextNode = currNode.getLink(char)
            if nextNode is None:
                nextNode = TrieNode(char)
                currNode.addLink(nextNode)
            currNode = nextNode

        currNode.setEnd()


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        maxLen = 0
        for word in words:
            self.trie.insertWord(word[::-1])
            maxLen = max(maxLen, len(word))

        self.maxsize = maxLen
        self.stream = []
        self.streamsize = 0

    def query(self, letter: str) -> bool:
        if self.streamsize == self.maxsize:
            self.stream = self.stream[1:]
            self.streamsize -= 1

        self.stream.append(letter)
        self.streamsize += 1

        node = None

        for i in range(len(self.stream) - 1, -1, -1):
            rootChar = self.stream[i]
            if node is None:
                node = self.trie.roots[ord(rootChar) - ord('a')]
            else:
                nextNode = node.getLink(rootChar)
                node = nextNode
            if node is None:
                break
            elif node.is_end:
                return True

        return False

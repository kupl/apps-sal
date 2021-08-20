from collections import deque


class TrieNode:

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.eow = False


class Trie:

    def __init__(self):
        self.rootTrie = TrieNode('*')
        self.currNode = self.rootTrie

    def addWord(self, word):
        self.currNode = self.rootTrie
        for (idx, char) in enumerate(word):
            if char not in self.currNode.children:
                charNode = TrieNode(char)
                self.currNode.children[char] = charNode
            self.currNode = self.currNode.children[char]
        self.currNode.eow = True

    def findNext(self, lettersQ):
        self.currNode = self.rootTrie
        for char in lettersQ:
            if char in self.currNode.children:
                self.currNode = self.currNode.children[char]
                if self.currNode.eow:
                    return True
            else:
                return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.streamTrie = Trie()
        self.lettersQ = deque()
        for word in words:
            self.streamTrie.addWord(word[::-1])

    def query(self, letter: str) -> bool:
        self.lettersQ.appendleft(letter)
        if len(self.lettersQ) > 2000:
            self.lettersQ.pop()
        return self.streamTrie.findNext(self.lettersQ)

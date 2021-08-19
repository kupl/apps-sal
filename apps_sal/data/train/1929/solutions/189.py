from collections import deque


class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEndWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        head = self.root
        for char in word:
            head = head.children.setdefault(char, TrieNode())
        head.isEndWord = True


class StreamChecker:

    def __init__(self, words):
        self.vocab = Trie()
        self.queue = deque()
        for word in words:
            self.vocab.addWord(word[::-1])

    def query(self, char):
        self.queue.appendleft(char)
        cur = self.vocab.root
        for c in self.queue:
            if c in cur.children:
                cur = cur.children[c]
                if cur.isEndWord:
                    return True
            else:
                break
        return False

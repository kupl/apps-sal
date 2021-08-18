import itertools


class TrieNode:
    def __init__(self):
        self.end = False
        self.nodes = {}

    def insert(self, word):
        if len(word) == 0:
            self.end = True
            return
        if word[0] not in self.nodes:
            self.nodes[word[0]] = TrieNode()
        self.nodes[word[0]].insert(word[1:])

    def startsWith(self, word):
        if len(word) == 0:
            return True
        if word[0] not in self.nodes:
            return False
        return self.nodes[word[0]].startsWith(word[1:])

    def exists(self, word):
        if self.end and len(word) == 0:
            return True
        if len(word) == 0 or word[0] not in self.nodes:
            return False
        return self.nodes[word[0]].exists(word[1:])


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.longest = 0
        for word in words:
            self.longest = max(self.longest, len(word))
            self.root.insert(word[::-1])
        self.word = ''

    def query(self, letter: str) -> bool:
        self.word = (self.word + letter)[-self.longest:]
        for i in range(len(self.word) - 1, -1, -1):
            other = self.word[i:][::-1]
            if not self.root.startsWith(other):
                break
            if self.root.exists(other):
                return True
        return False

from collections import deque


class Node:

    def __init__(self):
        self.isLast = False
        self.child = {}


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, ind, word, node=None):
        if node == None:
            node = self.root
        if ind == len(word):
            node.isLast = True
        else:
            if word[ind] not in node.child:
                node.child[word[ind]] = Node()
            self.insert(ind + 1, word, node.child[word[ind]])

    def isPrefix(self, ind, word, node=None):
        if node == None:
            node = self.root
        if node.isLast:
            return True
        if ind == len(word):
            return False
        if word[ind] in node.child:
            return self.isPrefix(ind + 1, word, node.child[word[ind]])
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(0, word[::-1])
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.isPrefix(0, self.stream)

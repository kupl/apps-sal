class Node:

    def __init__(self):
        self.child = {}
        self.isword = False


class Trie:

    def __init__(self):
        self.root = Node()

    def addword(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.isword = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.Trie = Trie()
        for word in words:
            self.Trie.addword(word[::-1])
        self.queue = []

    def query(self, letter: str) -> bool:
        self.queue.insert(0, letter)
        node = self.Trie.root
        for char in self.queue:
            if char not in node.child:
                return False
            else:
                node = node.child[char]
                if node.isword:
                    return True
        return False

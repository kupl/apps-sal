class TrieNode:
    def __init__(self):
        self.child = {}
        self.isword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode()
            node = node.child[w]
        node.isword = True

    def search(self, word):
        node = self.root
        for w in word:
            if w in node.child:
                if node.child[w].isword == True:
                    return True
                node = node.child[w]
            else:
                return False
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.stack = []
        self.size = max(len(word) for word in words)

    def query(self, letter: str) -> bool:
        if len(self.stack) >= self.size:
            self.stack.pop(0)
        self.stack.append(letter)
        return self.trie.search(''.join(self.stack[::-1]))


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])
        self.stream = ''

    def query(self, letter: str) -> bool:
        node = self.trie.root
        self.stream += letter
        for char in self.stream[::-1]:
            if char in node.c:
                node = node.c[char]
            else:
                break
            if node.isword:
                return True
        return False


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.c:
                node.c[char] = TrieNode(char)
            node = node.c[char]
        node.isword = True


class TrieNode:

    def __init__(self, v):
        self.v = v
        self.c = dict()
        self.isword = False

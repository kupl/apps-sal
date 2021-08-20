class TrieNode:

    def __init__(self):
        (self.children, self.end_node) = ({}, False)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = []
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        cur = self.trie.root
        for c in self.stream[::-1]:
            if c in cur.children:
                cur = cur.children[c]
                if cur.end_node:
                    return True
            else:
                break
        return False

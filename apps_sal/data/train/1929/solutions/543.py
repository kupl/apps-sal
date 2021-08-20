class Node:

    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.isWord = False


class Trie:

    def __init__(self, words):
        self.root = Node('')
        for word in words:
            p = self.root
            for ind in range(len(word) - 1, -1, -1):
                ch = word[ind]
                if p.children[ord(ch) - ord('a')] is None:
                    new_node = Node(ch)
                    p.children[ord(ch) - ord('a')] = new_node
                p = p.children[ord(ch) - ord('a')]
                if ind == 0:
                    p.isWord = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie(words)
        self.pointer_queue = []
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream.insert(0, letter)
        p = self.trie.root
        for ch in self.stream:
            if p.children[ord(ch) - ord('a')]:
                p = p.children[ord(ch) - ord('a')]
            else:
                return False
            if p.isWord:
                return True
        return False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends_here = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            curr = curr.children.setdefault(c, TrieNode())

        curr.ends_here = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.queue = deque()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        curr = self.trie.root

        for c in self.queue:
            if c in curr.children:
                curr = curr.children[c]
                if curr.ends_here:
                    return True

            else:
                break

        return False

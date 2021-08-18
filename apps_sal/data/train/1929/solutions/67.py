class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                new_node = TrieNode()
                curr.children[ch] = new_node
            curr = curr.children[ch]
        curr.is_end = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.addWord(reversed(word))
        self.queue = collections.deque()

    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        curr = self.trie.root
        for ch in self.queue:
            if ch not in curr.children:
                return False
            if ch in curr.children:
                curr = curr.children[ch]
                if curr.is_end:
                    return True

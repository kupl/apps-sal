class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_words(self, words):
        for word in words:
            cur = self.root
            for l in word:
                cur = cur.children[l]
            cur.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.trie.add_words([word[::-1] for word in words])
        self.prefix = ''

    def query(self, letter: str) -> bool:
        self.prefix += letter
        cur = self.trie.root
        for l in self.prefix[::-1]:
            if l not in cur.children:
                break
            cur = cur.children[l]
            if cur.is_word:
                return True
        return False

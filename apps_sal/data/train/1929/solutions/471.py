class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.currentMatch = frozenset([self.root])

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            if idx not in cur.children:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.isEnd = True

    @lru_cache(None)
    def matchNextChar(self, currentMatch, c):
        idx = ord(c) - ord('a')
        new_set = set([self.root])
        found = False
        for node in currentMatch:
            if idx in node.children:
                new_set.add(node.children[idx])
                if node.children[idx].isEnd:
                    found = True
        return (frozenset(new_set), found)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        (match, found) = self.trie.matchNextChar(self.trie.currentMatch, letter)
        self.trie.currentMatch = match
        return found

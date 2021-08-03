class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.isWord = True

    # def search(self, word):
    #     p = self.root
    #     for c in word:
    #         if c not in p.children:
    #             return False
    #         p = p.children[c]
    #     return p.isWord


class StreamChecker:

    def __init__(self, words: List[str]):
        self.queries = []
        self.trie = Trie()
        for word in words:
            self.trie.add(word[::-1])

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        p = self.trie.root
        for i in range(len(self.queries) - 1, -1, -1):
            c = self.queries[i]
            if c not in p.children:
                return False
            p = p.children[c]
            if p.isWord:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

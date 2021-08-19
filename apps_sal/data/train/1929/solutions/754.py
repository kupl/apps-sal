class TrieNode():
    import collections

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def construct(self, word):
        node = self.root
        for c in word[::-1]:
            node = node.children[c]
        node.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = Trie()
        self.letters = []
        for word in words:
            self.tree.construct(word)

    def query(self, letter: str) -> bool:
        self.letters.append(letter)

        if letter in self.tree.root.children:
            node = self.tree.root
            for l in self.letters[::-1]:
                node = node.children.get(l)
                if not node:
                    return False
                if node.is_word:
                    return True
            return node.is_word
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

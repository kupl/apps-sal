class Trie:
    def __init__(self):
        self.is_word = False
        self.child = defaultdict(Trie)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()  # root
        self.stream = ''
        for w in words:
            cur_node = self.trie
            for c in w[::-1]:
                # reverse char in word
                cur_node = cur_node.child[c]
            # last letter of word
            cur_node.is_word = True

    def query(self, letter: str) -> bool:

        self.stream += letter
        node = self.trie
        for c in reversed(self.stream):
            if c not in node.child:
                return False
            node = node.child[c]
            if node.is_word:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

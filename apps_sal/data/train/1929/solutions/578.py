class Trie:
    def __init__(self):
        self.is_word = False
        self.child = defaultdict(Trie)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = ''
        for w in words:
            cur_node = self.trie
            for c in w[::-1]:
                cur_node = cur_node.child[c]
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

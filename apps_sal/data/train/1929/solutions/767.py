class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        for word in words:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = dict()
                node = node[c]
            node['.'] = '.'

        self.curs = []

    def query(self, letter: str) -> bool:
        trie, curs = self.trie, self.curs

        curs = [cur[letter] for cur in curs if letter in cur]
        if letter in trie:
            curs.append(trie[letter])
        self.curs = curs

        return any('.' in cur for cur in curs)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

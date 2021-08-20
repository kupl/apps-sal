class Trie:

    def __init__(self, word, end):
        self.children = word
        self.end = end


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie({}, False)
        for word in words:
            cur = self.trie
            for char in word[::-1]:
                if not char in cur.children:
                    cur.children[char] = Trie({}, False)
                cur = cur.children[char]
            cur.end = True
        self.history = ''

    def query(self, letter: str) -> bool:
        self.history += letter
        streamer = self.trie
        for c in self.history[::-1]:
            if c not in streamer.children:
                return False
            elif streamer.children[c].end:
                return True
            streamer = streamer.children[c]
        return False

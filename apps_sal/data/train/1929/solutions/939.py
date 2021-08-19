def _trie():
    return collections.defaultdict(_trie)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = _trie()
        for word in words:
            trie = self.trie
            for c in word:
                if c not in trie:
                    trie[c] = _trie()
                trie = trie[c]
            trie['END']
        self.activePtr = []

    def query(self, letter: str) -> bool:
        matched = False
        if letter in self.trie:
            self.activePtr.append(self.trie)
        for (i, trie) in enumerate(self.activePtr):
            if letter in trie:
                trie = trie[letter]
                if 'END' in trie:
                    matched = True
                self.activePtr[i] = trie
            else:
                self.activePtr[i] = None
        self.activePtr = [t for t in self.activePtr if t is not None]
        return matched

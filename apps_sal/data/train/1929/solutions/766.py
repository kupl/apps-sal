class StreamChecker:

    def __init__(self, words: List[str]):
        from collections import defaultdict
        self.trie = dict()

        for word in words:
            trie = self.trie
            for c in word:
                if c not in trie:
                    trie[c] = dict()
                    trie[c]['word'] = False
                trie = trie[c]
            trie['word'] = True

        self.tries = list()

    def query(self, letter: str) -> bool:
        newtries = list()
        self.tries.append(self.trie)
        found = False
        for trie in self.tries:
            if letter in trie:
                newtries.append(trie[letter])
                if trie[letter]['word']:
                    found = True
        self.tries = newtries
        return found

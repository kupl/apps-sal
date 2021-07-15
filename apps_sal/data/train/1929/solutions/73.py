class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            d = self.trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['*'] = True
        self.open_words = []

    def query(self, letter: str) -> bool:
        found = False
        new_open_words = []
        if letter in self.trie:
            new_open_words.append(self.trie[letter])
            if '*' in self.trie[letter]:
                found = True
        for word in self.open_words:
            if letter in word:
                if '*' in word[letter]:
                    found = True
                new_open_words.append(word[letter])
        self.open_words = new_open_words
        return found

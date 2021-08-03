class StreamChecker:

    def build_trie(self, word: str) -> None:
        place = self.trie
        for ch in word:
            if ch in place:
                place = place[ch]
            else:
                place[ch] = dict()
                place = place[ch]
        place['*'] = None

    def __init__(self, words: List[str]) -> None:
        self.words = set(words)
        self.trie = dict()
        for word in words:
            self.build_trie(word)
        print((self.trie))
        self.temp = []
        self.temp2 = []

    def query(self, letter: str) -> bool:
        self.temp2 = []
        self.temp.append(self.trie)
        can = False
        for i in self.temp:
            if letter in i:
                self.temp2.append(i[letter])
                if '*' in i[letter]:
                    can = True
            else:
                continue
        self.temp = self.temp2
        return can

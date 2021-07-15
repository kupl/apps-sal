class StreamChecker:
    # TODO need proper Aho–Corasick
    # See also contest/weekly182/find-all-good-strings.python3.py
    # TLE, too many prefixes, hard to calculate shared suffixes
    # need a trie instead of set of words. Just building the set takes 2000^3

    def __init__(self, words: List[str]):
        _compress = {}
        _decompress = {}

        def compress(s):
            if s not in _compress:
                i = len(_compress)
                _compress[s] = i
                _decompress[i] = s
            return _compress[s]

        def decompress(i):
            return _decompress[i]

        compress(\"\")

        words = set(words)
        graph = defaultdict(
            lambda: defaultdict(int)
        )  # pref1 -> ch -> pref2 where pref2 is longest word that is a suffix of pref1
        prefs = set()
        for word in words:
            for i in range(len(word) + 1):
                pref = word[:i]
                prefs.add(pref)

        for pref in prefs:
            for i in range(26):
                ch = chr(ord(\"a\") + i)
                for j in range(len(pref) + 1):
                    pref2 = pref[j:] + ch
                    if pref2 in prefs and len(pref2) > len(
                        decompress(graph[compress(pref)][ch])
                    ):
                        graph[compress(pref)][ch] = compress(pref2)

        prefWithWordSuffix = set()
        for pref in prefs:
            for i in range(len(word) + 1):
                if pref[i:] in words:
                    prefWithWordSuffix.add(compress(pref))
                    break
        self.graph = graph
        self.state = compress(\"\")
        self.prefWithWordSuffix = prefWithWordSuffix
        # self.compress = compress
        # self.decompress = decompress

    def query(self, letter: str) -> bool:

        self.state = self.graph[self.state][letter]

        return self.state in self.prefWithWordSuffix


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[\"$\"] = word
        self.states = [self.trie]

    def query(self, letter: str) -> bool:
        nextStates = [self.trie]
        for state in self.states:
            if letter in state:
                nextStates.append(state[letter])
        self.states = nextStates
        # print(letter, [state['$'] for state in self.states if '$' in state])
        return any(\"$\" in state for state in self.states)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


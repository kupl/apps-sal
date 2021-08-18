class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = collections.defaultdict(dict)
        self.construct_trie(words)
        self.l = []

    def construct_trie(self, words):
        for word in words:
            t = self.trie
            for w in word:
                if(w not in t):
                    t[w] = {}
                t = t[w]
            t['$'] = True

        print((self.trie))

    def query(self, letter: str) -> bool:
        t = self.trie
        ans = False

        temp = []
        for d in self.l:
            if(letter in d):
                if('$' in d[letter]):
                    ans = True
                temp.append(d[letter])
        self.l = temp
        if(letter in t):
            self.l.append(t[letter])
            if('$' in t[letter]):
                return True
        return ans

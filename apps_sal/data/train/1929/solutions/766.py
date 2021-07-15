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
        #print(self.trie)
        # self.words = {word:0 for word in words}
        # self.possible = list()
        # self.maxsize = max([len(word) for word in words])

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
        # self.possible.append('')
        # newposs = list()
        # found = False
        # for pos in self.possible:
        #     pos += letter
        #     if pos in self.words:
        #         found = True
        #     if len(pos) <= self.maxsize:
        #         newposs.append(pos)
        # self.possible = newposs
        return found 


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            t = self.trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        self.poss = []

    def query(self, letter: str) -> bool:

        waitlist = []

        if letter in self.trie:
            waitlist.append(self.trie[letter])

        for t in self.poss:
            if letter in t:
                waitlist.append(t[letter])
        self.poss = waitlist
        return any('#' in t for t in waitlist)

#         ans = False
#         popthis = set()
#         if letter in self.trie:
#             t = self.trie
#             self.poss.append(t)
#         for i in range(len(self.poss)):
#             if letter in self.poss[i]:
#                 self.poss[i]=self.poss[i][letter]
#                 if '#' in self.poss[i]:
#                     ans = True
#             else:
#                 popthis.add(i)
#         new = []
#         for i,x in enumerate(self.poss):
#             if i not in popthis:
#                 new.append(x)
#         self.poss = new

#         return ans


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamC'hecker(words)
# param_1 = obj.query(letter)

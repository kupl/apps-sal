class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            t = self.trie
            for w in word:
                if w in t:
                    t = t[w]
                else:
                    t[w] = {}
                    t = t[w]
            t['$'] = word
        self.currWords = [self.trie]

    def query(self, letter: str) -> bool:
        q = self.currWords
        q.append(self.trie)
        newQ = []
        ans = False
        for node in q:
            if letter in node:
                if '$' in node[letter]:
                    ans = True
                newQ.append(node[letter])
        self.currWords = newQ
        return ans

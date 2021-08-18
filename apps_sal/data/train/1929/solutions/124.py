class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node


class StreamChecker_TLE:

    def _reinit(self):
        newdict = collections.defaultdict(list)
        for w in self.words:
            newdict[w[0]].append((w, 0))
        return newdict

    def __init__(self, words: List[str]):
        self.words = words
        self.curdict = self._reinit()
        self.refdict = self._reinit()

    def query(self, letter: str) -> bool:
        if not self.curdict[letter]:
            self.curdict = self._reinit()
            return False
        expect = self.curdict[letter][:]
        self.curdict = self._reinit()
        ret = False
        for w, idx in expect:
            idx += 1
            if idx == len(w):
                ret = True
            else:
                nxtch = w[idx]
                self.curdict[nxtch].append((w, idx))
        return ret

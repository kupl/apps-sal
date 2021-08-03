class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.q = ''
        for i in words:
            if i[-1] not in self.trie:
                self.trie[i[-1]] = [i[:-1]]
            else:
                self.trie[i[-1]].append(i[:-1])

    def query(self, letter: str) -> bool:

        trie = self.trie
        self.q += letter
        if letter not in trie:
            return False

        for i in trie[letter]:
            l = len(i)
            if self.q[-l - 1:-1] == i:
                return True

        return False

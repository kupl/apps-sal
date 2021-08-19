class StreamChecker:

    def __init__(self, words: List[str]):
        self.waitList = []
        self.trie = {}
        for w in words:
            curr = self.trie
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = {'#'}

    def query(self, letter: str) -> bool:
        newWaitList = []
        if letter in self.trie:
            newWaitList.append(self.trie[letter])
        for ele in self.waitList:
            if letter in ele:
                newWaitList.append(ele[letter])
        self.waitList = newWaitList
        for ele in self.waitList:
            if '#' in ele:
                return True
        return False

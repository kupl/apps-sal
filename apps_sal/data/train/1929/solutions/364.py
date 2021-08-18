class StreamChecker:
    def __init__(self, words: List[str]):

        self.now = ''
        self.trie = defaultdict()

        for w in words:
            cur = self.trie
            for i in w[::-1]:
                if i not in cur:
                    cur[i] = defaultdict()

                cur = cur[i]
            cur['

    def query(self, letter: str) -> bool:
        self.now += letter

        s = self.now[::-1]
        cur = self.trie
        for i in s:
            if i in cur:
                cur = cur[i]
                if '
                    return True
            else:
                break
        return False

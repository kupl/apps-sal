class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            cur = self.trie
            for l in reversed(w):
                if l not in cur:
                    cur[l] = {}
                cur = cur[l]
            cur[\"#\"] = True
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        #print(self.stream)
        cur = self.trie
        for l in self.stream:
            #print(l)
            if l in cur:
                cur = cur[l]
                #print(\"cur:\",cur)
            else:
                break
            if \"#\" in cur: return True
        return False

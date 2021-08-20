class TrieNode:

    def __init__(self):
        self.kids = {}
        self.isWord = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.q = collections.deque(maxlen=max((len(x) for x in words)))
        self.root = TrieNode()
        for x in words:
            cur = self.root
            for c in x[::-1]:
                if c not in cur.kids:
                    cur.kids[c] = TrieNode()
                cur = cur.kids[c]
                if cur.isWord:
                    break
            cur.isWord = True

    def query(self, letter: str) -> bool:

        def helper(word):
            cur = self.root
            for c in word:
                if c in cur.kids:
                    cur = cur.kids[c]
                    if cur.isWord:
                        return True
                else:
                    return False
            return False
        self.q.appendleft(letter)
        cur = self.root
        for c in self.q:
            if c in cur.kids:
                cur = cur.kids[c]
                if cur.isWord:
                    return True
            else:
                return False
        return False

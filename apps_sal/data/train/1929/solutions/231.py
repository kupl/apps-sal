class Trie():
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

    def insert(self, s):
        curr = self
        for c in s:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = Trie()
            curr = curr.children[ord(c) - ord('a')]
        curr.endOfWord = True

    def search(self, s):
        curr = self
        for c in s:
            if curr.children[ord(c) - ord('a')] == None:
                return False
            curr = curr.children[ord(c) - ord('a')]
            if curr.endOfWord == True:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        self.stream = collections.deque()
        for w in words:
            self.t.insert(reversed(w))

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.t.search(self.stream)

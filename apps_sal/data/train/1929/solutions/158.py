class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def insert(self, word):
        cur = self
        for letter in word:
            if cur.children[ord(letter) - ord('a')] == None:
                cur.children[ord(letter) - ord('a')] = Trie()
            cur = cur.children[ord(letter) - ord('a')]
        cur.end = True

    def search(self, s):
        cur = self
        for letter in s:
            if cur.children[ord(letter) - ord('a')] == None:
                return False
            cur = cur.children[ord(letter) - ord('a')]
            if cur.end == True:
                return True
        return False


class StreamChecker:
    from collections import deque

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.words = words
        self.q = deque()
        for word in self.words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.q.appendleft(letter)
        return self.trie.search(self.q)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

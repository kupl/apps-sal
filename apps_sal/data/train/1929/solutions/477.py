class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.letters = ''
        for word in words:
            self.insert(word)

    def query(self, letter: str) -> bool:
        self.letters += letter
        curr = self.root
        for i in range(len(self.letters) - 1, -1, -1):
            if curr.child[ord(self.letters[i]) - ord('a')] == None:
                return False
            curr = curr.child[ord(self.letters[i]) - ord('a')]
            if curr.end:
                return True
        return False

    def insert(self, word):
        curr = self.root
        for i in range(len(word) - 1, -1, -1):
            c = word[i]
            nextt = curr.child[ord(c) - ord('a')]
            if nextt == None:
                nextt = Trie()
                curr.child[ord(c) - ord('a')] = nextt
            curr = curr.child[ord(c) - ord('a')]
        curr.end = True


class Trie:

    def __init__(self):
        self.end = False
        self.child = [None for i in range(26)]

class Tri:
    def __init__(self):
        self.root = TriNode()

    def add(self, word):
        node = self.root

        for letter in word:
            if letter not in node.__next__:
                node.next[letter] = TriNode()

            node = node.next[letter]

        node.isWord = True

    def check(self, letters):
        node = self.root

        for letter in letters:
            if node.isWord:
                return True

            if letter not in node.__next__:
                return False

            node = node.next[letter]

        if node.isWord:
            return True

        return False


class TriNode:
    def __init__(self):
        self.next = {}
        self.isWord = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.tri = Tri()
        self.recent = []
        self.maxLength = -1
        self.length = 0

        for word in words:
            if len(word) > self.maxLength:
                maxLength = len(word)

            self.tri.add(word[::-1])

    def query(self, letter: str) -> bool:
        if self.length == self.maxLength:
            self.recent.pop()
            self.recent.insert(0, letter)
        else:
            self.recent.insert(0, letter)
            self.length += 1

        return self.tri.check(self.recent)

class TrieNode:

    def __init__(self):
        self._values = set()
        self.next = None

    def insert(self, value):
        self._values.add(value)

    def has(self, value):
        return value in self._values


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.q = ''
        self.chars = set()
        self.words = set()
        for word in words:
            curr = self.root
            for index in range(len(word) - 1, -1, -1):
                char = word[index]
                curr.insert(char)
                self.chars.add(char)
                if not curr.__next__:
                    curr.next = TrieNode()
                curr = curr.__next__
            self.words.add(word)

    def query(self, letter: str) -> bool:
        if letter not in self.chars:
            self.q = ''
            return False
        self.q = letter + self.q
        curr = self.root
        sub_q = ''
        for char in self.q:
            if not curr.has(char):
                return False
            sub_q = char + sub_q
            if sub_q in self.words:
                return True
            curr = curr.__next__
        return False

class Node:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def add(self, val):
        self.children[val] = Node()

    def has(self, val):
        return val in list(self.children.keys())

    def get(self, val):
        return self.children[val]

    def set_terminal(self):
        self.terminal = True

    def is_terminal(self):
        return len(self.children) == 0 or self.terminal


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = Node()
        for word in words:
            curr = self.root
            for sym in word[::-1]:
                if not(curr.has(sym)):
                    curr.add(sym)
                curr = curr.get(sym)
            curr.set_terminal()
        self.prefix = ''

    def query(self, letter: str) -> bool:
        self.prefix += letter
        curr = self.root
        for sym in self.prefix[::-1]:
            if not(curr.has(sym)):
                return False
            curr = curr.get(sym)
            if curr.is_terminal():
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

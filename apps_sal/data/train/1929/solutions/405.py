class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = Tree()
        for item in words:
            curr = self.tree
            for letter in item[::-1]:
                if letter not in curr.subtrees:
                    curr.subtrees[letter] = Tree()
                curr = curr.subtrees[letter]
            curr.food = True
        self.q = ''

    def query(self, letter: str) -> bool:
        self.q += letter
        reverse_q = self.q[::-1]
        curr = self.tree
        for letter in reverse_q:
            if letter not in curr.subtrees:
                return False
            else:
                curr = curr.subtrees[letter]
                if curr.food:
                    return True
        return False


class Tree:

    def __init__(self):
        self.food = False
        self.subtrees = {}

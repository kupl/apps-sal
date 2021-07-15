class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = Tree('0', [])
        for item in words:
            curr = self.tree
            for letter in item[::-1]:
                result = curr.in_list(letter)
                if result is None:
                    curr.subtrees.append(Tree(letter, []))
                    curr = curr.subtrees[-1]
                else:
                    curr = curr.subtrees[result]
            curr.food = True
        self.q = ''

    def query(self, letter: str) -> bool:
        self.q += letter
        reverse_q = self.q[::-1]
        curr = self.tree
        for letter in reverse_q:
            result = curr.in_list(letter)
            if result is None:
                return False
            else:
                curr = curr.subtrees[result]
                if curr.food:
                    return True
        return False


class Tree:
    def __init__(self, root, subtrees: List):
        self.root = root
        self.food = False
        self.subtrees = subtrees

    def in_list(self, letter: str):
        for i, item in enumerate(self.subtrees):
            if item.root == letter:
                return i
        return None

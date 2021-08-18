class TreeNode:
    def __init__(self):
        self.children = {}
        self.isend = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TreeNode()
        self.char_so_far = deque()
        for word in words:
            node = self.root
            for char in word[::-1]:
                if char not in node.children:
                    node.children[char] = TreeNode()
                node = node.children[char]
            node.isend = True

    def check_word(self, l):
        node = self.root
        for char in l:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.isend:
                return True
        return node.isend

    def query(self, letter: str) -> bool:
        node = self.root
        self.char_so_far.appendleft(letter)
        return self.check_word(self.char_so_far)

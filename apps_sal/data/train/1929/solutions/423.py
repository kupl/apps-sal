from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, node):
        self.children.append(node)


class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TreeNode(0)
        self.max_len = 0
        for w in words:
            self.max_len = max(self.max_len, len(w))
            self.make_trie(w)
        self.history = deque([])

    def make_trie(self, word):
        parent = self.root
        for char in word[::-1]:
            current = None
            for node in parent.children:
                if node.val == char:
                    current = node
            if not current:
                current = TreeNode(char)
                parent.add_child(current)
            parent = current
        parent.add_child(TreeNode('.'))

    def query(self, letter: str) -> bool:
        self.history.append(letter)
        if len(self.history) > self.max_len:
            self.history.popleft()
        parent = self.root
        for i in range(len(self.history) - 1, -1, -1):
            char = self.history[i]
            if i < len(self.history) - 1 and any([child.val == '.' for child in parent.children]):
                return True
            found = False
            for node in parent.children:
                if node.val == char:
                    found = True
                    parent = node
            if not found:
                return False
        return any([child.val == '.' for child in parent.children])

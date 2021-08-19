class TreeNode:
    def __init__(self):
        self.dict = defaultdict(TreeNode)
        self.result = False


class StreamChecker:
    def __init__(self, words: List[str]):
        self.tree = TreeNode()
        self.text = ''
        for word in words:
            curr = self.tree
            for c in word[::-1]:
                curr = curr.dict[c]
            curr.result = True

    def query(self, letter: str) -> bool:
        self.text += letter
        curr = self.tree
        for c in self.text[::-1]:
            if c not in curr.dict:
                break
            curr = curr.dict[c]
            if curr.result:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)



class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            curr = self.root
            for c in word:
                curr = curr.setdefault(c, {})
            curr['$'] = '$'
        self.stack = [self.root]

    def query(self, letter: str) -> bool:
        stack = []
        flag = False
        for node in self.stack:
            child = node.get(letter)
            if child:
                stack.append(child)
                flag |= '$' in child
        self.stack = stack
        self.stack.append(self.root)
        return flag

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

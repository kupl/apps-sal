
class TreeNode:
    def __init__(self, val=0):
        self.val = 0
        self.children = [None] * 26


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TreeNode(0)
        for word in words:
            word = word[::-1]
            current = self.root
            for letter in word:
                temp = current.children[ord(letter) - ord('a')]
                if temp is None:
                    new = TreeNode(0)
                    current.children[ord(letter) - ord('a')] = new
                    current = new
                else:
                    current = temp
            current.val = 1
        self.query_str = ''

    def query(self, letter: str) -> bool:
        self.query_str = letter + self.query_str
        return self.search()

    def search(self):
        current = self.root
        for letter in self.query_str:
            temp = current.children[ord(letter) - ord('a')]
            if temp is None:
                return False
            else:
                if temp.val == 1:
                    return True
                else:
                    current = temp


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

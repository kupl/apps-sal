class Solution:

    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        self.idx = 0
        return self.recoverTree(S, 0)

    def recoverTree(self, s, depth):
        d = self.getDepth(s)
        if d != depth:
            self.idx -= d
            return
        root = TreeNode(self.getVal(s))
        root.left = self.recoverTree(s, depth + 1)
        root.right = self.recoverTree(s, depth + 1)
        return root

    def getDepth(self, s):
        d = 0
        while self.idx < len(s) and s[self.idx] == '-':
            d += 1
            self.idx += 1
        return d

    def getVal(self, s):
        num = 0
        while self.idx < len(s) and s[self.idx].isdigit():
            num = num * 10 + int(s[self.idx])
            self.idx += 1
        return num

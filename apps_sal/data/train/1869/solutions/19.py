class Solution:

    def recoverFromPreorder(self, S: str) -> TreeNode:
        return self.helper(S, 0)

    def helper(self, S, level):
        if not S:
            return None
        val = self.get(S)
        node = TreeNode(val)
        (idx1, idx2) = self.find(S, level)
        if idx1:
            node.left = self.helper(S[idx1:idx2], level + 1)
        if idx2:
            node.right = self.helper(S[idx2:], level + 1)
        return node

    def find(self, S, level):
        idx1 = idx2 = None
        count = 0
        for (i, ch) in enumerate(S):
            if ch != '-':
                if count == level + 1:
                    if not idx1:
                        idx1 = i
                    else:
                        idx2 = i
                        return (idx1, idx2)
                count = 0
            else:
                count += 1
        return (idx1, idx2)

    def get(self, S):
        val = ''
        for ch in S:
            if ch == '-':
                break
            val += ch
        return val

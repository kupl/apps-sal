class Solution:

    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.i = 0
        return self.construct_tree(S, 0)

    def construct_tree(self, S, level):
        if self.i == len(S):
            return None
        zero = ord('0')
        j = self.i
        node_lvl = 0
        while j < len(S) and S[j] == '-':
            node_lvl += 1
            j += 1
        val = 0
        while j < len(S) and S[j].isdigit():
            val = val * 10 + (ord(S[j]) - zero)
            j += 1
        if level != node_lvl:
            return None
        self.i = j
        return TreeNode(val, self.construct_tree(S, level + 1), self.construct_tree(S, level + 1))

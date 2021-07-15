# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def transform(self, string):
        s = string.split('-')
        i = 1
        res = [(s[0], 0)]
        while i < len(s):
            l = 1
            if s[i] == '':
                while s[i] == '':
                    i += 1
                    l += 1
            res.append((int(s[i]), l))
            i += 1
        return res

    def recoverFromPreorder(self, S: str) -> TreeNode:
        L = {}
        trans = self.transform(S)
        L[0] = (TreeNode(trans[0][0]))
        for val, lvl in trans[1:]:
            L[lvl] = TreeNode(val)
            
            if L[lvl - 1].left:
                L[lvl - 1].right = L[lvl]
            else:
                L[lvl - 1].left = L[lvl]
        return L[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        i = 0
        d = 0
        s = []
        v = 0
        while i < len(S) and S[i].isdigit():
            v = v * 10 + int(S[i])
            i += 1
        root = TreeNode(v)
        s.append((root, d))
        while i < len(S):
            if S[i].isdigit():
                v = 0
                while i < len(S) and S[i].isdigit():
                    v = v * 10 + int(S[i])
                    i += 1
                nnode = TreeNode(v)
                if not s:
                    s.append((nnode, d))
                else:
                    node = s.pop()
                    while s and node[1] != d - 1:
                        node = s.pop()

                    if not node[0].left:
                        node[0].left = nnode
                        s.append(node)
                        # s.append((nnode, d))
                    else:
                        node[0].right = nnode
                    s.append((nnode, d))
            else:
                d = 0
                while i < len(S) and S[i] == '-':
                    d += 1
                    i += 1
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, A: List[int]) -> TreeNode:
        A.reverse()

        def build(lower=-math.inf, upper=math.inf):
            if not A or A[-1] < lower or A[-1] > upper:
                return None

            root = TreeNode(A.pop())
            root.left = build(lower, root.val)
            root.right = build(root.val, upper)
            return root
        return build()

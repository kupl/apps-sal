# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        o = {}

        def str_original(node):
            if not node:
                return '(None)'
            if node not in o:
                left = str_original(node.left)
                mid = '({})'.format(node.val)
                right = str_original(node.right)
                o[node] = '({}){}({})'.format(left, mid, right)
            return o[node]
        str_original(original)
        c = {}
        self.res = None

        def str_cloned(node):
            if not node:
                return '(None)'
            if node not in c:
                left = str_cloned(node.left)
                mid = '({})'.format(node.val)
                right = str_cloned(node.right)
                c[node] = '({}){}({})'.format(left, mid, right)
            if c[node] == o[target]:
                self.res = node
            return c[node]
        str_cloned(cloned)
        # print(o[target])

        return self.res

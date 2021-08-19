# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, path):
            if node.left == None and node.right == None:
                res[0] = max(res[0], max([abs(j - node.val) for j in path]))
                return

            else:
                if len(path) > 0:
                    res[0] = max(res[0], max([abs(j - node.val) for j in path]))

                if node.left:
                    dfs(node.left, path + [node.val])

                if node.right:
                    dfs(node.right, path + [node.val])

                return

        res = [-1 * float('infinity')]

        dfs(root, [])

        print(res)

        return res[0]

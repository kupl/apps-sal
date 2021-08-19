# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ret = []

        def dfs(node, parent):
            if node:
                if node.val in to_delete:
                    node.left = dfs(node.left, False)
                    node.right = dfs(node.right, False)
                else:
                    if not parent:
                        ret.append(node)
                    node.left = dfs(node.left, True)
                    node.right = dfs(node.right, True)
                    return node
        dfs(root, False)
        return ret

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # APP1: convert to_delete to a set, divide and conquer to get left, right.
    # dfs: 1 return child root, None if child deleted.
    # 2. check if cur in delete, pass it for recursion call
    # 3 check if child is deleted, delete the link to children
    # Runtime: 98%
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        res, to_delete = [], set(to_delete)
        self.dfs(root, res, to_delete, True)
        return res

    def dfs(self, root, res, to_delete, parent_deleted):
        if not root:
            return None
        if parent_deleted and root.val not in to_delete:
            res.append(root)

        root_deleted = True if root.val in to_delete else False
        root.left = self.dfs(root.left, res, to_delete, root_deleted)
        root.right = self.dfs(root.right, res, to_delete, root_deleted)
        return None if root_deleted else root

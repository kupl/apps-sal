# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans, to_delete = [], set(to_delete)
        def search(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete
            if is_root and not root_deleted:
                ans.append(root)
            root.left = search(root.left, root_deleted)
            root.right = search(root.right, root_deleted)
            return None if root_deleted else root
        search(root, True)
        return ans

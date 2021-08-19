# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return
        tovisit = []
        result = []
        if root in to_delete:
            if root.left is not None:
                tovisit.append(root.left)
                result.append(root.left)
            if root.right is not None:
                tovisit.append(root.right)
                result.append(root.right)
        else:
            tovisit.append(root)
            result.append(root)

        while len(tovisit) > 0:
            new_tovisit = []
            for item in tovisit:
                if item.val in to_delete:
                    if item.left is not None:
                        result.append(item.left)
                    if item.right is not None:
                        result.append(item.right)
                    if item in result:
                        result.remove(item)
                if item.left is not None:
                    new_tovisit.append(item.left)
                    if item.left.val in to_delete:
                        item.left = None
                if item.right is not None:
                    new_tovisit.append(item.right)
                    if item.right.val in to_delete:
                        item.right = None
            tovisit = new_tovisit
        return result

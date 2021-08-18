
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def findNode(root):
            if root.val == target.val:
                return root
            else:
                if root.left is None and root.right is None:
                    return None
                if root.left is not None:
                    left = findNode(root.left)
                    if left is not None:
                        return left
                if root.right is not None:
                    right = findNode(root.right)
                    if right is not None:
                        return right

        return findNode(cloned)

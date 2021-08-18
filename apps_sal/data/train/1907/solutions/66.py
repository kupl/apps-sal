
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def inorder(root1, root2, target):
            if root1 == target:
                return root2
            if root1.left:
                left = inorder(root1.left, root2.left, target)
                if left:
                    return left
            if root1.right:
                right = inorder(root1.right, root2.right, target)
                if right:
                    return right
            return None

        return inorder(original, cloned, target)

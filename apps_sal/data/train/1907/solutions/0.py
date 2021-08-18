
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def getnode(root):
            if not root:
                return None
            elif root.val == target.val:
                return root
            else:
                return getnode(root.left) or getnode(root.right)
        return getnode(cloned)


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original:
            if original == target:
                return cloned
            if original.left:
                outnode = self.getTargetCopy(original.left, cloned.left, target)
                if outnode:
                    return outnode
            if original.right:
                outnode = self.getTargetCopy(original.right, cloned.right, target)
                if outnode:
                    return outnode

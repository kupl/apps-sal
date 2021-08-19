class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or not cloned:
            return None
        stack = []
        stack.append((original, cloned))
        while stack:
            (orig, clone) = stack.pop()
            if orig == target:
                return clone
            if orig.right:
                stack.append((orig.right, clone.right))
            if orig.left:
                stack.append((orig.left, clone.left))

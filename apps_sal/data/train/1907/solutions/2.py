class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        while stack or cloned:
            while cloned:
                stack.append(cloned)
                cloned = cloned.left
            cloned = stack.pop()
            if cloned.val == target.val:
                return cloned
            cloned = cloned.right
        return None

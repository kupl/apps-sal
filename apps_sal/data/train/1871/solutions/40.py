class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val, root.val)]
        maxDiff = -1
        while stack:
            node, maxVal, minVal = stack.pop()
            maxVal = max(maxVal, node.val)
            minVal = min(minVal, node.val)
            maxDiff = max(maxDiff, maxVal - minVal)
            if node.left:
                stack.append((node.left, maxVal, minVal))
            if node.right:
                stack.append((node.right, maxVal, minVal))
        return maxDiff

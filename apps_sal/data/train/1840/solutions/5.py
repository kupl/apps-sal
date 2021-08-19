class Solution:

    def helper(self, node: TreeNode, lastDirection: str, cache) -> int:
        if not node:
            return 0
        if (node, lastDirection) in cache:
            return cache[node, lastDirection]
        count = 1
        childCount = float('-inf')
        if lastDirection == 'right':
            childCount = max(childCount, self.helper(node.left, 'left', cache))
        else:
            childCount = max(childCount, self.helper(node.right, 'right', cache))
        count += childCount
        cache[node, lastDirection] = count
        return count

    def longestZigZag(self, root: TreeNode) -> int:
        maxCount = float('-inf')
        cache = {}
        stack = [root]
        while stack:
            node = stack.pop()
            maxCount = max(maxCount, self.helper(node, 'left', cache))
            maxCount = max(maxCount, self.helper(node, 'right', cache))
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return maxCount - 1

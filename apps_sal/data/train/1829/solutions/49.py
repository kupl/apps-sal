class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, root.val)]
        while len(stack) > 0:
            popped = stack.pop()
            node = popped[0]
            curMax = popped[1]
            if node.val >= curMax:
                count += 1
            if node.right is not None:
                stack.append((node.right, max(node.right.val, curMax)))
            if node.left is not None:
                stack.append((node.left, max(node.left.val, curMax)))
        return count

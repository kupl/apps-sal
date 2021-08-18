class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, root.val)]
        count = 0

        while stack:
            cur, greatest = stack.pop()
            if cur:
                if cur.val >= greatest:
                    count += 1

                if cur.right:
                    stack.append((cur.right, max(cur.right.val, greatest)))
                if cur.left:
                    stack.append((cur.left, max(cur.left.val, greatest)))

        return count

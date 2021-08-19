class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        level = 0
        max_level = 0
        max_sum = float('-inf')
        q = []
        q.append(root)
        while q:
            level += 1
            curr = 0
            for _ in range(len(q)):
                node = q.pop(0)
                curr += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_sum < curr:
                max_sum = curr
                max_level = level
        return max_level

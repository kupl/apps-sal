class Solution:

    def goodNodes(self, root: TreeNode) -> int:

        def helper(root: TreeNode, maxVal: int, count: List[int]):
            if not root:
                return
            else:
                if root.val >= maxVal:
                    count[0] += 1
                helper(root.left, max(maxVal, root.val), count)
                helper(root.right, max(maxVal, root.val), count)
        count = [0]
        helper(root, -math.inf, count)
        return count[0]

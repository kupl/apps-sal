class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        memo = {}
        self.maxLevelSumHelper(root, memo, 1)
        maxValue = max(memo.values())
        targetKeys = [k for k in memo if memo[k] == maxValue]
        return min(targetKeys)

    def maxLevelSumHelper(self, node, memo, depth):
        if node == None:
            return
        if depth in memo:
            memo[depth] += node.val
        else:
            memo[depth] = node.val
        self.maxLevelSumHelper(node.left, memo, depth + 1)
        self.maxLevelSumHelper(node.right, memo, depth + 1)
        return

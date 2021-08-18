class Solution:
    def levelSumHelper(self, node, level, sums):
        if node is None:
            return sums
        if(len(sums) == level):
            sums.append(node.val)
        else:
            sums[level] += node.val
        sums = self.levelSumHelper(node.left, level + 1, sums)
        sums = self.levelSumHelper(node.right, level + 1, sums)
        return sums

    def maxLevelSum(self, root: TreeNode) -> int:
        sums = self.levelSumHelper(root, 0, [])
        m = sums[0]
        ret = 0
        for i, s in enumerate(sums):
            if s > m:
                m = s
                ret = i
        return ret + 1

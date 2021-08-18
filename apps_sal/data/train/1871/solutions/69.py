class Solution:
    def helper(self, root, output, maxValue):
        if(root is None):
            return
        for ele in output:
            if(abs(root.val - ele) > maxValue[0]):
                maxValue[0] = abs(root.val - ele)
        output.append(root.val)
        self.helper(root.left, output, maxValue)
        self.helper(root.right, output, maxValue)
        output.pop()

    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxValue = [0]
        output = list()
        self.helper(root, output, maxValue)
        return maxValue[0]

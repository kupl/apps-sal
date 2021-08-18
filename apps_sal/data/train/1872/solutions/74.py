class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxVal = root.val
        ans = level = 1
        stack = [root]
        while True:
            nextStack = []
            level += 1
            sumVal = 0
            for item in stack:
                if item.left:
                    sumVal += item.left.val
                    nextStack.append(item.left)
                if item.right:
                    sumVal += item.right.val
                    nextStack.append(item.right)
            if nextStack:
                stack = nextStack
                if sumVal > maxVal:
                    maxVal = sumVal
                    ans = level
            else:
                break

        return ans

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        curLevel = maxLevel = 1
        output = root.val

        while queue:
            s, nextLevel = 0, []
            for n in queue:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
                s += n.val
            if s > output:
                output = s
                maxLevel = curLevel
            curLevel += 1
            queue = nextLevel
        return maxLevel

class Solution:

    def maxLevelSum(self, root: TreeNode) -> int:
        stack = [[root, 1]]
        l = []
        while stack:
            ele = stack.pop()
            node = ele[0]
            val = ele[1]
            if node:
                stack.append([node.left, val + 1])
                stack.append([node.right, val + 1])
                if len(l) < val:
                    l.append(node.val)
                else:
                    l[val - 1] += node.val
        maxx = max(l)
        for i in range(len(l)):
            if l[i] == maxx:
                return i + 1

import collections


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        total, maxLevel = 0, 0

        def helper(node, level):
            if not node:
                return
            nonlocal total
            nonlocal maxLevel
            print((total, maxLevel, node.val, level))
            if level > maxLevel:
                print(('here', level, maxLevel))
                total = node.val
                maxLevel = level
            elif level == maxLevel:
                total += node.val

            helper(node.left, level + 1)
            helper(node.right, level + 1)

        helper(root, 0)
        print(total)
        return total

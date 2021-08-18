from collections import defaultdict


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        treeDict = defaultdict(list)

        def treeLevel(root, level):
            if not root:
                return
            else:
                treeDict[level].append(root.val)

            treeLevel(root.left, level + 1)
            treeLevel(root.right, level + 1)

        treeLevel(root, 0)

        return sum(treeDict[list(treeDict.keys())[-1]])

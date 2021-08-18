class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        maxDiff = 0
        stk = [root]
        ancDict = {}
        ancDict[root.val] = []
        while len(stk) != 0:
            root = stk.pop()
            if root.left is not None:
                stk.append(root.left)
                if root.left not in ancDict:
                    ancDict[root.left.val] = []
                ancDict[root.left.val].append(root.val)
                ancDict[root.left.val].extend(ancDict[root.val])
            if root.right is not None:
                stk.append(root.right)
                if root.right not in ancDict:
                    ancDict[root.right.val] = []
                ancDict[root.right.val].append(root.val)
                ancDict[root.right.val].extend(ancDict[root.val])
        for k in ancDict:
            for v in ancDict[k]:
                if abs(v - k) > maxDiff:
                    maxDiff = abs(v - k)
        return maxDiff

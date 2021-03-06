class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        s = {}

        def check(root, depth, s):
            if root == None:
                return 0
            if depth not in s:
                s[depth] = [root.val]
            else:
                s[depth].append(root.val)
            check(root.left, depth + 1, s)
            check(root.right, depth + 1, s)
            return s
        check(root, 0, s)
        m = max(s.keys())
        return sum(s[m])

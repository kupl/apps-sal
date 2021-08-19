class Solution:

    def minCameraCover(self, root: TreeNode) -> int:
        dump1 = {}
        dump2 = {}

        def f(root):
            if root == None:
                return 0
            if root in dump1:
                return dump1[root]
            ans = 1 + min(f(root.left), g(root.left, True)) + min(f(root.right), g(root.right, True))
            dump1[root] = ans
            return ans

        def g(root, covered):
            if root == None:
                return 0
            if (root, covered) in dump2:
                return dump2[root, covered]
            if root.left == None and root.right == None:
                if covered:
                    return 0
                return float('inf')
            ans = float('inf')
            if not covered:
                if root.left != None:
                    ans = f(root.left) + min(g(root.right, False), f(root.right))
                if root.right != None:
                    ans = min(ans, f(root.right) + min(f(root.left), g(root.left, False)))
            else:
                ans = min(f(root.left), g(root.left, False)) + min(f(root.right), g(root.right, False))
            dump2[root, covered] = ans
            return ans
        if root.left == None and root.right == None:
            return 1
        return min(f(root), g(root, False))

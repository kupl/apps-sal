class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def check(root):
            r = chr(root.val + 97)
            if root.left == None and root.right == None:
                return [r]

            r1 = []
            r2 = []
            if root.left != None:
                r1 = check(root.left)
            if root.right != None:
                r2 = check(root.right)
            rtv = []
            small = min(r1 + r2)
            for x in r1 + r2:
                if x.startswith(small):
                    rtv.append(x + r)
            rtv.insert(0, small + r)

            return rtv
            pass

        rtv = check(root)
        return min(rtv)

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def maxDepth(rt):
            root = rt
            if root == None:
                return 0
            stack_list = [(root, 1)]
            maxh = 1
            if root.left == None and root.right == None:
                return maxh

            while len(stack_list) != 0:

                r, v = stack_list.pop()
                if r.right == None and r.left == None:
                    if v > maxh:
                        maxh = v

                if r.left != None:
                    stack_list.append((r.left, v + 1))
                if r.right != None:
                    stack_list.append((r.right, v + 1))
            return maxh
        htmax = maxDepth(root)

        if htmax == 0:
            return 0

        stack_list = [(root, 1)]
        dmax = 0
        if root.left == None and root.right == None:
            return root.val

        maxh = 1
        while len(stack_list) != 0:

            r, v = stack_list.pop()
            if r.right == None and r.left == None:
                if v > maxh:
                    maxh = v

            if r.left != None:
                stack_list.append((r.left, v + 1))
                if v + 1 == htmax:
                    dmax = dmax + r.left.val

            if r.right != None:
                stack_list.append((r.right, v + 1))
                if v + 1 == htmax:
                    dmax = dmax + r.right.val
        return dmax

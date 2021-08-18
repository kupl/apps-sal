class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        stack = [(root, True)]
        res = []
        while stack:
            curr, toBeRoot = stack.pop()
            if curr:
                if curr.val not in to_delete and toBeRoot:
                    res.append(curr)
                toBeRoot = curr.val in to_delete
                stack += [(curr.left, toBeRoot), (curr.right, toBeRoot)]
                if curr.left and curr.left.val in to_delete:
                    curr.left = None
                if curr.right and curr.right.val in to_delete:
                    curr.right = None

        return res

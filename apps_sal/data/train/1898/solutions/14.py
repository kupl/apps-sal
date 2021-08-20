class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        results = []

        def dft(root, to_delete):
            if not root:
                return
            dft(root.left, to_delete)
            dft(root.right, to_delete)
            if root.left and root.left.val in to_delete:
                root.left = None
            if root.right and root.right.val in to_delete:
                root.right = None
            if root.val in to_delete:
                print(root.val)
                if root.right:
                    print(root.right.val)
                    results.append(root.right)
                    root.right = None
                if root.left:
                    print(root.left.val)
                    results.append(root.left)
                    root.left = None
        dft(root, to_delete)
        if root.val not in to_delete:
            results.append(root)
        return results

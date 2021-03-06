class Solution:

    def delete(self, root, to_delete, parent, res):
        if not root:
            return root
        elif parent:
            if root.val in to_delete:
                root.left = self.delete(root.left, to_delete, False, res)
                root.right = self.delete(root.right, to_delete, False, res)
                return None
            else:
                root.left = self.delete(root.left, to_delete, True, res)
                root.right = self.delete(root.right, to_delete, True, res)
                return root
        elif root.val in to_delete:
            root.left = self.delete(root.left, to_delete, False, res)
            root.right = self.delete(root.right, to_delete, False, res)
            return None
        else:
            res.append(root)
            root.left = self.delete(root.left, to_delete, True, res)
            root.right = self.delete(root.right, to_delete, True, res)
            return root

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        root = self.delete(root, set(to_delete), False, res)
        return res

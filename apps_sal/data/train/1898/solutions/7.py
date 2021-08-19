# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        roots = []
        roots.append(root)

        def removeRoot(root, roots):
            index = 0
            for i in roots:
                if i == root:
                    roots.pop(index)
                index += 1

        def delete(root, prev, roots, to_delete):
            left = root.left
            right = root.right
            if root.val in to_delete:
                removeRoot(root, roots)
                if left:
                    roots.append(root.left)
                if right:
                    roots.append(root.right)
                root.left = None
                root.right = None
                if prev:
                    if prev.left == root:
                        prev.left = None
                    if prev.right == root:
                        prev.right = None

            if left:
                delete(left, root, roots, to_delete)
            if right:
                delete(right, root, roots, to_delete)

        delete(root, None, roots, to_delete)
        return roots

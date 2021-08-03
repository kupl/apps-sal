# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []

        deleted = set()
        for node in to_delete:
            deleted.add(node)

        out = []
        self.bfs(root, deleted, out)
        return out

    def bfs(self, root, deleted, out):
        q = Queue()
        q.put((root, True))

        while q.qsize() > 0:
            node, parent_delete = q.get()

            if node.val in deleted:
                curr_delete = True
            else:
                curr_delete = False

            if node.left:
                q.put((node.left, curr_delete))
                if node.left.val in deleted:
                    node.left = None

            if node.right:
                q.put((node.right, curr_delete))
                if node.right.val in deleted:
                    node.right = None

            if curr_delete:
                node.left = None
                node.right = None
            elif parent_delete:
                out.append(node)

class Solution:

    def _iter(self, root):
        if root is not None:
            yield root
            yield from self._iter(root.left)
            yield from self._iter(root.right)

    def _search(self, head, root):
        if head is None or root is None:
            return head is None
        elif head.val == root.val:
            return self._search(head.next, root.left) or self._search(head.next, root.right)
        else:
            return False

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        for node in self._iter(root):
            if node.val == head.val:
                if self._search(head, node):
                    return True
        return False

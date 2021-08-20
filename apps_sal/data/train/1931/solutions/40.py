class Solution:

    def matchPath(self, head, root):
        if head is None:
            return True
        if root is None:
            return False
        if head.val != root.val:
            return False
        if self.matchPath(head.next, root.left):
            return True
        if self.matchPath(head.next, root.right):
            return True
        return False

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        nexts = [root]
        while len(nexts) > 0:
            node = nexts.pop()
            if node.val == head.val:
                if self.matchPath(head, node):
                    return True
            if node.left:
                nexts.append(node.left)
            if node.right:
                nexts.append(node.right)
        return False

class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode, path=None, cool=None) -> bool:
        path = path or []
        cool = cool or []
        path.append(root.val)
        cool_n = []
        for i in cool:
            if i.val == root.val:
                cool_n.append(i.__next__)
                if cool_n[-1] == None:
                    return True
        cool = cool_n
        if root.val == head.val:
            cool.append(head.__next__)
            if cool[-1] == None:
                return True
        l = r = False
        if root.left:
            l = self.isSubPath(head, root.left, path.copy(), cool)
            if l is True:
                return True
        if root.right:
            r = self.isSubPath(head, root.right, path.copy(), cool)
            if r is True:
                return True
        if root.left is None and root.right is None:
            cool = []
        return False

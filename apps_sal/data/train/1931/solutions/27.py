class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head == None:
            return 1
        if root == None:
            return 0
        self.arr = []

        def trav(root, val):
            if root:
                if root.val == val:
                    self.arr.append(root)
                trav(root.left, val)
                trav(root.right, val)
        trav(root, head.val)
        p = head
        while self.arr:
            p = p.next
            if p == None:
                return 1
            i = 0
            r = len(self.arr)
            while i < r:
                node = self.arr.pop(0)
                if node.left:
                    if node.left.val == p.val:
                        self.arr.append(node.left)
                if node.right:
                    if node.right.val == p.val:
                        self.arr.append(node.right)
                i += 1
        return 0

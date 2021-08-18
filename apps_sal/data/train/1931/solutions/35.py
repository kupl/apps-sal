class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        helper = set()

        def getStart(p):
            if p:
                if p.val == head.val:
                    helper.add(p)
                getStart(p.left)
                getStart(p.right)

        getStart(root)

        while head.next:
            new = set()
            for node in helper:
                if node.val == head.val:
                    if node.left:
                        new.add(node.left)
                    if node.right:
                        new.add(node.right)
            helper = new

            if not helper:
                return False

            head = head.next

        return (head.val in [node.val for node in helper])

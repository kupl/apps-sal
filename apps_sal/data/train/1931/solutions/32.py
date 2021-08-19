class Solution:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root and (not head) or (not root and head):
            return False
        elif root and (not head):
            return True
        memory = []

        def preorder(node: ListNode):
            if not node:
                return
            nonlocal head
            nonlocal memory
            if node.val == head.val:
                memory.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        head = head.__next__
        while head and memory:
            newMemory = []
            for node in memory:
                if node.left and node.left.val == head.val:
                    newMemory.append(node.left)
                if node.right and node.right.val == head.val:
                    newMemory.append(node.right)
            head = head.__next__
            memory = newMemory
        return len(memory) > 0

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        visited = set()

        def checkNode(treePointer, listPointer):
            if listPointer == None:
                return True
            if treePointer == None and listPointer != None:
                return False

            if (treePointer, listPointer) in visited:
                return False

            if treePointer.val == listPointer.val:
                if checkNode(treePointer.left, listPointer.next) or checkNode(treePointer.right, listPointer.next):
                    return True

            if treePointer.val == head.val:
                if checkNode(treePointer.left, head.next) or checkNode(treePointer.right, head.next):
                    return True

            if checkNode(treePointer.left, head) or checkNode(treePointer.right, head):
                return True

            visited.add((treePointer, listPointer))
            return False

        return checkNode(root, head)

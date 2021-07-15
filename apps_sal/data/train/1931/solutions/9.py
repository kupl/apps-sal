class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root:
            return self.traverse(root, head)
        
    def traverse(self, cur, head):
        if self.startwith(cur, head):
            return True
        else:
            if cur.left and self.traverse(cur.left, head):
                return True
            elif cur.right and self.traverse(cur.right, head):
                return True
        return False
    
    def startwith(self, startnode, head) -> bool:
        if startnode.val == head.val:
            if head.next == None:
                return True
            if startnode.left and self.startwith(startnode.left, head.next):
                return True
            elif startnode.right and self.startwith(startnode.right, head.next):
                return True
            False
        else:
            return False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        def rec(head,root,connected):
            if not head or not root:
                return False
            if connected and head.val==root.val:
                if head.__next__:
                    left=rec(head.__next__,root.left,True)
                    right=rec(head.__next__,root.right,True)
                    return left or right
                else:
                    return True
            if head.val!=root.val and connected:
                return False
            if not connected:
                if head.val==root.val:
                    left_noConn=rec(head,root.left,False)
                    right_noConn=rec(head,root.right,False)
                    if head.__next__:
                        left=rec(head.__next__,root.left,True)
                        right=rec(head.__next__,root.right,True)
                    else:
                        return True
                    return left or right or left_noConn or right_noConn
                else:
                    left_noConn=rec(head,root.left,False)
                    right_noConn=rec(head,root.right,False)
                    return left_noConn or right_noConn
                
                return left or right
        
        return rec(head,root,False)
            


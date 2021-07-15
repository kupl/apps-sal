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
        def checker(l1, l2):
            if len(l1) < len(l2): return False
            
            for i in range(len(l2)):
                if l2[len(l2)-1-i] != l1[len(l1)-1-i]: return False
            return True
        
        pattern = []
        while(head):
            pattern.append(head.val)
            head = head.next
        
        self.res = False
        def traverse(root, S=[]):
            if self.res: return True
            if root == None: return False
            if checker(S+[root.val], pattern): 
                self.res = True
                return True
            traverse(root.left, S+[root.val])
            traverse(root.right, S+[root.val])
        
        traverse(root)
        return self.res

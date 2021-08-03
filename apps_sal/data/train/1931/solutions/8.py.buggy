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
    
    def traverse(self, head: ListNode, node:ListNode, root: TreeNode) -> bool:
        if not node:
            return True
        if not root:
            return False
        print(\"comparing \" + str(root.val) + \" with \" + str(node.val))
        res = root.val == node.val
        if res:
            node = node.next
        else:
            node = head
            if root.val == node.val:
                node = node.next
        res = self.traverse(head, node, root.left)
        res = res or self.traverse(head, node, root.right)
        return res
    
    def find(self, node: ListNode, root: TreeNode) -> bool:
        if not node:
            return True
        if not root:
            return False
        print(\"comparing \" + str(root.val) + \" with \" + str(node.val))
        if node.val == root.val:
            return self.find(node.next, root.left) or self.find(node.next, root.right)
        return False
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        # if not root or not head:
        #     return False
        # return self.traverse(head, head, root)
        if not root:
            return False
        check = head.val == root.val
        if check and (self.find(head.next, root.left) or self.find(head.next, root.right)):
            return True
        else:
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

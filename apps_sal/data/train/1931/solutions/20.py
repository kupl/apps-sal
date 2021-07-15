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
        target = \"\"
        while head:
            target = target + str(head.val)
            head = head.next
            #print(target) # LList is a str = 428

        def dfs(root, path):
            # print(path) #1426 1428
            if target in path: # matched
                return True      
            if root.left:
                ans =  dfs(root.left, path + str(root.left.val))
                if ans:  #if ans == True:
                    return True          
            if root.right:
                ans  = dfs(root.right, path + str(root.right.val))
                if ans: return True       
            return False            
        return dfs(root, str(root.val))
        
            
        

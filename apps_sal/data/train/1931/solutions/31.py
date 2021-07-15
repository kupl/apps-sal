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
        # 6:39 10/7/20
        
        # BFS + DFS
        
        def dfs(node):
            if not node:
                return
            if node.val == head.val:
                q.appendleft((node, head, set()))
            dfs(node.left)
            dfs(node.right)
        
        # Step 1: Use DFS to add every node that has the same value with that of head to a queue
        q = collections.deque()
        dfs(root)
        
        # Step 2: Use BFS to walk down the path where both node and linked list have the same value
        while q:
            tree_node, list_node, visited = q.pop()
            if tree_node.val == list_node.val:
                if not list_node.__next__:  
                    return True # Finally, we reached the end of linked list. 
                for nei in (tree_node.left, tree_node.right):
                    if nei and nei not in visited and nei.val == list_node.next.val:
                        visited.add(nei)
                        q.appendleft((nei, list_node.__next__, visited))
                        visited.remove(nei)
        return False
        

            
           
                    


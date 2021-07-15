# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 
 class Solution:
     def kthSmallest(self, root, k):
         """
         :type root: TreeNode
         :type k: int
         :rtype: int
         """
         return self.use_in_order_count_iteration(root, k)
     
     def use_binary_search(self, root, k):
         # if tree is a balanced BST
         count = self.count_tree(root.left)
         if count + 1 == k:
             return root.val
         if count + 1 > k:
             return self.use_binary_search(root.left, k)
         else:
             return self.use_binary_search(root.right, k - count - 1)
         
     def count_tree(self, node):
         if not node:
             return 0
         return 1 + self.count_tree(node.left) + self.count_tree(node.right)
     
     def use_in_order_count(self, root, k):
         self.count = k
         self.ret = root.val
         self.in_order_count(root, k)
         return self.ret
     
     def use_in_order_count_iteration(self, root, k):
         
         stack = collections.deque()
         curr = root
         count = k
         ret = root.val
         while stack or curr:
             while curr:
                 stack.append(curr)
                 curr = curr.left
             node = stack.pop()
             count -= 1
             if count == 0:
                 ret = node.val
                 break
             curr = node.right
         return ret
     
     def in_order_count(self, node, k):
         if not node:
             return
         self.in_order_count(node.left, k)
         self.count -= 1
         if self.count == 0:
             self.ret = node.val
             return
         self.in_order_count(node.right, k)
     
     def use_in_order(self, root, k):
         self.data = []
         self.in_order(root)
         return self.data[k-1]
     
     def in_order(self, root):
         if not root:
             return
         self.in_order(root.left)
         self.data.append(root.val)
         self.in_order(root.right)

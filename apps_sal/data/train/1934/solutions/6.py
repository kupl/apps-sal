# Definition for a binary tree node.
 # class TreeNode:
 #     def __init__(self, x):
 #         self.val = x
 #         self.left = None
 #         self.right = None
 from collections import defaultdict
 from queue import Queue
 
 class Solution:
   def zigzagLevelOrder(self, root):
     """
     :type root: TreeNode
     :rtype: List[List[int]]
     """
     if not root:
       return []
     node_level = {root: 0}
     level_nodes = defaultdict(lambda: [])
     # Group nodes by level in BFS order
     q = Queue()
     q.put(root)
     level_nodes[0].append(root)
     while not q.empty():
       node = q.get()
       child_level = node_level[node] + 1
       if node.left:
         node_level[node.left] = child_level
         level_nodes[child_level].append(node.left)
         q.put(node.left)
       if node.right:
         node_level[node.right] = child_level
         level_nodes[child_level].append(node.right)
         q.put(node.right)
     # Go through nodes level by level
     level_nodes_pairs = sorted(list(level_nodes.items()))
     result = []
     for (level, nodes) in level_nodes_pairs:
       if level % 2 == 0:
         # Left to right
         result.append([node.val for node in nodes])
       else:
         # Right to left
         result.append([node.val for node in reversed(nodes)])
     return result
     


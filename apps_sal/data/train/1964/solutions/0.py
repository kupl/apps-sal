def get_tree_height(node, parent_node_height):
     if node is None:
         return 0
     node.height = parent_node_height + 1
     if node.left is None and node.right is None:
         return 1
     return max(get_tree_height(node.left, node.height), get_tree_height(node.right, node.height)) + 1
 
 def fill_in_array(result, node, root_index, width):
     if node is None:
         return
     result[node.height - 1][root_index] = str(node.val)
     new_width = width // 2
     fill_in_array(result, node.left, root_index - new_width // 2 - 1, new_width)
     fill_in_array(result, node.right, root_index + new_width // 2 + 1, new_width)
 
 class Solution:
     def printTree(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[str]]
         """
         height = get_tree_height(root, 0)
         rows = height
         cols = 0
         for i in range(height):
             cols = cols * 2 + 1
         result = [[""] * cols for _ in range(rows)]
         fill_in_array(result, root, cols // 2, cols)
         return result

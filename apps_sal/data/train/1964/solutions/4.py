class Solution:
     def printTree(self, root):
         """
         :type root: TreeNode
         :rtype: List[List[str]]
         """
         #The length of the entries should be 2^height - 1
         #The root will always be at the center
         #Recurse on the left and right subtrees pass the new centers and the lengths
         height = 0
         
         #O(n)
         def Dfs(node, currHeight):
             nonlocal height
             if node == None:
                 height = max(currHeight-1, height)
                 return
             Dfs(node.left, currHeight+1)
             Dfs(node.right, currHeight+1)
         Dfs(root, 1)
         
         #O(nlogn)
         ret = [[""]*(2**height - 1) for _ in range(height)]
         
         #O(n)
         def rec(node, currHeight, start, end):
             if(node == None):
                 return
             center = int((start + end)/2)
             ret[currHeight][center] = str(node.val)
             rec(node.left, currHeight+1, start, center-1)
             rec(node.right, currHeight+1, center+1, end)
         rec(root, 0, 0, 2**height-1)
         return ret

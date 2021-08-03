# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return traverse_tree(cloned, target.val)
        
  

def traverse_tree(node: TreeNode, val: int) -> TreeNode:
    xNode = None
    
    if node == None:
        return;

    print(node.val);

    if node.val == val:
           print(\"cr {}\".format(node.val))
           return node

    xNode = traverse_tree(node.left, val)
    if xNode != None:
            print(\"left {}\".format(xNode))
            return xNode
    xNode = traverse_tree(node.right, val)
    if xNode != None:
            print(\"right {}\".format(xNode))
            return xNode
    
    print(\"Not found \")
    
    return None


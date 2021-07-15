# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        deepest = [[]]
        max_depth = [0]
        self.mark_depth_and_parent(root, deepest, max_depth)
        # print(f\"DEEPEST : {[n.val for n in deepest[0]]} @ DEPTH = {max_depth[0]}\")
        return self.get_lca(deepest[0])
        
    
    def mark_depth_and_parent(self, root, deepest, max_depth, depth=0, parent=None):
        if not root:
            return
        
        # print(f\"{root.val} | Depth : {depth}\")
        if depth > max_depth[0]:
            max_depth[0] = depth
            deepest[0] = [root]
        elif depth == max_depth[0]:
            deepest[0].append(root)
            
        root.depth = depth
        root.parent = parent
        self.mark_depth_and_parent(root.left, deepest, max_depth, depth + 1, root)
        self.mark_depth_and_parent(root.right, deepest, max_depth, depth + 1, root)
        
    def get_lca(self, deepest):
        while len(deepest) > 1:
            n1, n2 = deepest.pop(), deepest.pop()
            while n1 and n1.depth > n2.depth:
                n1 = n1.parent
            while n2 and n2.depth > n1.depth:
                n2 = n2.parent
            while n1 != n2:
                n1 = n1.parent
                n2 = n2.parent
            deepest.append(n1)
        return deepest[0]



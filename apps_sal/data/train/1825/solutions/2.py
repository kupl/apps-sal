# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        # get all paths
        paths = []
        def dfs(n, ps):
            nonlocal paths
            
            if not n:
                return
            if not n.left and not n.right:
                paths.append((len(ps), ps + [n]))
            if n.left:
                dfs(n.left, ps + [n])
            if n.right:
                dfs(n.right, ps + [n])
                
        dfs(root, [])
        # print(paths)
        
        # get longest paths
        paths = sorted(paths, key=lambda x: x[0], reverse=True)
        longest = []
        depth, path = paths[0]
        for d, p in paths:
            if d == depth:
                longest.append(p)
        # print([[x.val for x in xs] for xs in longest])
        
        # get the lowest common parent node
        if len(longest) == 1:
            return path[-1]
        for i in range(len(path)):
            if any(path[i] != p[i] for p in longest):
                break
        return path[i-1]
                
        
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def helper(node):
            # at each node, return depth, lca
            if not node: return 0, None
            h1, lca1 = helper(node.left)
            h2, lca2 = helper(node.right)
            if h1 > h2: return h1+1, lca1
            if h2 > h1: return h2+1, lca2
            if h1 == h2: return h1+1, node
        
        return helper(root)[1]
            


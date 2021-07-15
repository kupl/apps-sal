# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        # build undirected graph so we can treat both parent and child nodes as
        # neighbors for easy traversal
        graph = collections.defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)
        
        # for each possible y, we do DFS from x to find how many nodes our 
        # opponent can reach from x. Note that our opponent will not be able to
        # reach any nodes in the subtree rooted at y. If our opponent cannot 
        # reach at least half of all nodes (i.e. n//2), we will win for sure.
        for y in range(1, n+1):
            if y != x:
                visited = set()
                stack = [x]
                while stack:
                    val = stack.pop()
                    visited.add(val)
                    for nei in graph[val]:
                        if nei not in visited and nei != y:
                            stack.append(nei)

                if len(visited) <= n//2:
                    return True
        
        return False
                        
                    
            
                
        
            
            


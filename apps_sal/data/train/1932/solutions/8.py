# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        graph = defaultdict(list)

        def dfs(s):
            if not s:
                return
            for child in [s.left, s.right]:
                if not child:
                    continue
                graph[child.val].append(s.val)
                graph[s.val].append(child.val)
                dfs(child)
        dfs(root)

        visited = set()
        visited.add(x)

        def dfs_graph(u):
            res = 1
            visited.add(u)
            for nei in graph[u]:
                if nei not in visited:
                    res += dfs_graph(nei)
            return res

        candidates = [dfs_graph(nei) for nei in graph[x]]
        if not candidates:
            return False
        res = max(candidates)

        if res > n - res:
            return True
        else:
            return False

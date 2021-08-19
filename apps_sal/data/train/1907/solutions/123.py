visited = set()


def dfs(cloned, target):
    if cloned.val not in visited:
        visited.add(cloned)
        if cloned.val == target.val:
            print(cloned)
            return cloned
        if cloned.left:
            a = dfs(cloned.left, target)
            if a:
                return a
        if cloned.right:
            a = dfs(cloned.right, target)
            if a:
                return a


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        found = dfs(cloned, target)
        return found


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]
        visited = set()

        while queue:
            node = queue.pop()
            if node:
                if node.val == target.val:
                    return node
                if node not in visited:
                    visited.add(node)
                    queue.append(node.left)
                    queue.append(node.right)
        return False

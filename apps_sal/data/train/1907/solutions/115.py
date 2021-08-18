
class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        queue = []
        queue.append(cloned)

        while queue:

            node = queue.pop(0)

            if node.val == target.val:
                return node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return None

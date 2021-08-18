
class Solution:
    cloned_target = None

    def traverse_tree(self, node, target):
        if not node:
            return
        if self.cloned_target is not None:
            return
        if node.val == target.val:
            self.cloned_target = node
            return
        self.traverse_tree(node.left, target)
        self.traverse_tree(node.right, target)

    def itr_traverse_tree(self, node, target):
        nodes_level = [node]
        while len(nodes_level) > 0:
            curr_node = nodes_level.pop()
            if curr_node is not None and target.val == curr_node.val:
                return curr_node
            if curr_node.left:
                nodes_level.append(curr_node.left)
            if curr_node.right:
                nodes_level.append(curr_node.right)
        return None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.itr_traverse_tree(cloned, target)

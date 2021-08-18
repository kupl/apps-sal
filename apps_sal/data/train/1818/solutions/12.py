class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        lists = self.recursiveSmallest(root)
        min_list = min(lists)
        return ''.join(min_list)

    def recursiveSmallest(self, node: TreeNode) -> List[str]:
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [self.convert(node.val)]
        lists = []
        if node.left:
            smallest_left = self.recursiveSmallest(node.left)
            lists.extend(smallest_left)
        if node.right:
            smallest_right = self.recursiveSmallest(node.right)
            lists.extend(smallest_right)
        return [l + self.convert(node.val) for l in lists]

    def convert(self, value: int) -> str:
        a_value = ord('a')
        return chr(a_value + value)

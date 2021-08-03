# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        def helper(node, v):
            if node is None:
                return
            node.val = v
            if node.left:
                helper(node.left, v * 2 + 1)
            if node.right:
                helper(node.right, v * 2 + 2)
            return
        self.root = root
        helper(root, 0)
        print((self.root))
        return

    def find(self, target: int) -> bool:
        target += 1
        s = target
        l = 0
        while target > 0:
            target = target >> 1
            l += 1
        node = self.root
        c = 0
        print((bin(s)))
        for c in range(1, l)[::-1]:  # 2, 1 for 111
            k = s & (1 << (c - 1))
            print(k)
            if k:
                if node.right:
                    node = node.right
                    print((node.val, s - 1))
                else:
                    return False
            else:
                if node.left:
                    node = node.left
                else:
                    return False
        return node and node.val == s - 1


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

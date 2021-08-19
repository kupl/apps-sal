# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        root = self.recover(root)
        self.root = root
        self.inorder = self.Inorder(root)

    def recover(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        if root.left:
            root.left.val = 2 * root.val + 1
        if root.right:
            root.right.val = 2 * root.val + 2

        self.recover(root.left)
        self.recover(root.right)

        return root

    def Inorder(self, root):
        lis = []
        if root:
            lis = self.Inorder(root.left)
            lis.append(root.val)
            lis = lis + self.Inorder(root.right)

        return lis

    def find(self, target: int) -> bool:
        root = self.root
        lis = self.inorder
        lis.sort()

        return self.binarySearch(lis, 0, len(lis) - 1, target)

    def binarySearch(self, lis: List[int], l: int, r: int, target: int) -> bool:
        if r >= l:
            mid = l + (r - l) // 2
            if lis[mid] == target:
                return True
            elif lis[mid] > target:
                return self.binarySearch(lis, l, mid - 1, target)
            else:
                return self.binarySearch(lis, mid + 1, r, target)
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

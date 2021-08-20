class Solution:

    def helper(self, root, output, count):
        if root is None:
            return
        flag = False
        for ele in output:
            if ele > root.val:
                flag = True
        if flag == False:
            count[0] += 1
        output.append(root.val)
        self.helper(root.left, output, count)
        self.helper(root.right, output, count)
        output.pop()

    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        output = []
        self.helper(root, output, count)
        return count[0]

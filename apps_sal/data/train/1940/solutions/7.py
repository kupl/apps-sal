class Solution:

    def nextLargerNodes(self, head):
        stack = []
        res = []
        vals = []
        ind = 0
        while True:
            res += [0]
            while len(stack) > 0 and vals[stack[-1]] < head.val:
                res[stack[-1]] = head.val
                stack.pop()
            stack += [ind]
            vals += [head.val]
            ind += 1
            if head.__next__ is not None:
                head = head.__next__
            else:
                break
        return res

class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        output = []
        stack = []
        curr = head
        while curr:
            while stack and stack[-1][1] < curr.val:
                output[stack.pop()[0]] = curr.val
            stack.append([len(output), curr.val])
            output.append(0)
            curr = curr.__next__
        return output

class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        curr = head
        prev = None
        while curr != None:
            temp = curr.__next__
            curr.next = prev
            prev = curr
            curr = temp
        curr = prev
        stack = [0]
        l = []
        while curr != None:
            if stack[-1] > curr.val:
                l.append(stack[-1])
            else:
                while stack[-1] <= curr.val and stack[-1] != 0:
                    stack.pop()
                l.append(stack[-1])
            stack.append(curr.val)
            curr = curr.__next__
        return l[::-1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        node = head
        ans = []
        stack = []
        i = 0
        while node is not None:
            # print(i, stack, ans)
            ans.append(0)
            if len(stack):
                while len(stack) and node.val > stack[-1][1]:
                    j = stack[-1][0]
                    ans[j] = node.val
                    # print(j, ans[j])
                    stack.pop()
            stack.append((i, node.val))
            node = node.__next__
            i += 1
        return ans


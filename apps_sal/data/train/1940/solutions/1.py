# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        cur, nodes = head, []
        while cur:
            nodes += [cur.val]
            cur = cur.next

        out = [0] * len(nodes)
        stack = []
        for i in range(len(out)):

            while len(stack) and nodes[stack[-1]] < nodes[i]:
                out[stack.pop()] = nodes[i]
            stack.append(i)
        return out

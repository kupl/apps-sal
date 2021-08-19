# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 转化成stack 来做
        if not head:
            return head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.__next__
        stack = []
        res = [0 for _ in range(len(val_list))]
        for i in range(len(val_list)):
            while stack and val_list[stack[-1]] < val_list[i]:
                res[stack.pop()] = val_list[i]
            stack.append(i)
        return res

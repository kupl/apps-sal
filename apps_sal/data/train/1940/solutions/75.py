# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 借鉴自 discuss
        pos = 0
        ans = []
        stack = []  # 单调栈（递减）
        while head:
            ans.append(0)
            # 退栈的时候更新 ans 数组
            while stack and stack[-1][1] < head.val:
                idx, _ = stack.pop()
                ans[idx] = head.val
            
            stack.append((pos, head.val))
            head = head.next
            pos += 1

        return ans

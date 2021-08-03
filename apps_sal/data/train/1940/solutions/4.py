# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 用stack存一个递减列表，每次遇到大的数就出栈，同时更新stack中存的index对应的output
        if head is None:
            return []
        if head.next is None:
            return [0]

        i = head
        stack = []
        out = []
        count = 0
        while i:
            # print('node ', i.val)
            if not stack:
                stack.append([count, i.val])
            elif i.val <= stack[-1][1]:
                stack.append([count, i.val])
            else:
                while stack and i.val > stack[-1][1]:
                    tmp_count, tmp_val = stack.pop()
                    out.append([tmp_count, i.val])
                stack.append([count, i.val])
            # print(stack, out)
            i = i.next
            count += 1

        output = [0] * count
        for i, j in out:
            output[i] = j
        return output

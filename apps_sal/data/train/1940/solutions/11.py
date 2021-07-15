# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        n = len(nums)
        idx = [n] * n
        ans = [0] * n
        for i in reversed(range(0, n - 1, 1)):
            cur = i + 1
            while cur < n:
                if nums[cur] <= nums[i]:
                    cur = idx[cur]
                else:
                    ans[i] = nums[cur]
                    idx[i] = cur
                    break

        return ans

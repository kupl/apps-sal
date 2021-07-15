# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.__next__
        
        st = []
        ans = [0]* len(nums)
        for i in range(len(nums)):
            while st and nums[st[-1]] < nums[i]:
                ans[st[-1]] = nums[i]
                st.pop()
            st.append(i)
        
         
        return ans
                    

            
                
        
            


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        def dfs(head, i):
            if not head:
                return
            if head.val in G:
                G[head.val] = i
            dfs(head.next, i + 1)
        G = collections.Counter(G)
        ans = 1
        dfs(head, 0)
        sortedValues = sorted(G.values())
        for i in range(1, len(sortedValues)):
            if sortedValues[i] != sortedValues[i - 1] + 1:
                ans += 1
        return ans

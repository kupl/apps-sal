# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:

        temp = head
        new = []

        while temp:
            new.append(temp.val)
            temp = temp.__next__

        dkg = {}

        for i in G:
            dkg[i] = 1

        for i in range(len(new)):
            if new[i] in dkg:
                new[i] = 1
            else:
                new[i] = 0

        count = new[0]
        for i in range(1, len(new)):
            if new[i] != new[i - 1] and new[i] == 1:
                count += 1

        return count

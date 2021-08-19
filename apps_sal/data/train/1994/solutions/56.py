# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents_v1(self, head: ListNode, G: List[int]) -> int:

        # traverse list & count conn-comp
        count = 0               # keep track of number of comps
        new_comp = False        # flag if a new comp is in progress
        while head:

            # filter out elements not in G
            if head.val in G:
                # a new comp detected
                if not new_comp:
                    new_comp = True
                    count += 1
            else:
                # flag the current comp (if in progress) is done
                new_comp = False

            # try next element
            head = head.__next__

        return count

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        return self.numComponents_v1(head, G)

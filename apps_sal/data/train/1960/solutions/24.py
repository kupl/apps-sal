class linkedNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        head = linkedNode(-1)
        pointer = head
        for i in range(1, m + 1):
            newLN = linkedNode(i)
            newLN.prev = pointer
            pointer.next = newLN
            pointer = pointer.next
        pointer.next = linkedNode(-1)
        pointer.next.prev = pointer
        ans = []
        for query in queries:
            i = 0
            pointer = head.next
            while pointer.val != query:
                pointer = pointer.next
                i += 1
            ans.append(i)
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev
            pointer.next = head.next
            head.next.prev = pointer
            head.next = pointer
            pointer.prev = head
        return ans

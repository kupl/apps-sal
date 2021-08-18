class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        dummy = ListNode(0)
        hash = {0: dummy}
        dummy.next = head
        sum = 0
        i = head
        while i:
            sum += i.val
            if sum in list(hash.keys()):
                tempsum = sum
                j = hash[sum].__next__
                while j != i:
                    tempsum += j.val
                    del hash[tempsum]
                    j = j.__next__
                hash[sum].next = i.__next__
            else:
                hash[sum] = i
            i = i.__next__

        return dummy.__next__

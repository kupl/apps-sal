class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        l = []
        result = head
        while head != None:
            num = head.val
            bFlag = False
            if num == 0:
                bFlag = True
                if result == head:
                    result = head.next
                else:
                    l[len(l) - 1].next = head.next
            else:
                for i in range(len(l) - 1, -1, -1):
                    num += l[i].val
                    if num == 0:
                        bFlag = True
                        if i == 0:
                            result = head.next
                        else:
                            l[i - 1].next = head.next
                        for j in range(len(l) - 1, i - 1, -1):
                            l.pop()
                        break
            if bFlag == False:
                l.append(head)
            head = head.next
        return result

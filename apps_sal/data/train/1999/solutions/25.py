class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        a = []
        temp = head
        while(temp):
            a.append(temp.val)
            temp = temp.next
        l = len(a)
        i = l - 1
        x = 0
        ind = []
        while(i >= 1):
            e = a[i]
            j = i - 1
            while(j >= 0):
                e += a[j]
                if e == 0:
                    ind.append((j, i))
                    i = j
                    break
                j -= 1
            i -= 1
        li = len(ind)
        j = 0
        while(j < li):
            s, e = ind[j][0], ind[j][1]
            for i in range(e, s - 1, -1):
                a.pop(i)

            j += 1
        h = ListNode(0)
        temp = h
        while a:
            e = a.pop(0)
            if e != 0:
                temp.next = ListNode(e)
                temp = temp.next
        return h.next

class Solution:

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        while True:
            n = head
            size = 0
            while n != None:
                size += 1
                n = n.__next__
            i = 0
            flag = False
            while i < size:
                node = head
                k = 0
                prev = head
                while k < i:
                    prev = node
                    if node == None:
                        break
                    node = node.__next__
                    k += 1
                i += 1
                curr_sum = 0
                n = prev
                d = {}
                while node != None:
                    curr_sum += node.val
                    if curr_sum == 0:
                        if i == 1:
                            head = node.__next__
                        else:
                            n.next = node.__next__
                        flag = True
                        break
                    node = node.__next__
            if not flag:
                break
        return head

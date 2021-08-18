class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = []
        if head == None:
            return result
        l = []
        result.append(0)
        l.append(head.val)
        head = head.next
        index = 0
        while head != None:
            index = len(l) - 1
            while index >= 0:
                if head.val > l[index]:
                    for i in range(len(result) - 1, -1, -1):
                        if result[i] == 0:
                            result[i] = head.val
                            break
                    index -= 1
                    l.pop()
                else:
                    break
            result.append(0)
            l.append(head.val)
            head = head.next
        return result

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        def removeZeros(arr):
            for i in range(len(arr)):
                tsum = 0
                for j in range(i, len(arr)):
                    tsum += arr[j]
                    if tsum == 0:
                        return True, [i, j]

            return False, [len(arr), len(arr) - 1]

        arr = []
        current = head
        while current is not None:
            arr.append(current.val)
            current = current.__next__

        ret = removeZeros(arr)
        flag = ret[0]
        while flag:
            start = ret[1][0]
            end = ret[1][1]
            arr = arr[:start] + arr[end + 1:]
            ret = removeZeros(arr)
            flag = ret[0]

        head = None
        current = head
        for n in arr:
            if current is None:
                current = ListNode(n)
                head = current
            else:
                current.next = ListNode(n)
                current = current.__next__

        return head

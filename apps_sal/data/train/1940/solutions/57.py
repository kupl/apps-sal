class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        ptr = head
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.__next__
        result = [0] * len(arr)
        s = []
        for i in range(len(arr) - 1, -1, -1):
            while len(s) > 0 and s[-1] <= arr[i]:
                s.pop()
            result[i] = 0 if len(s) == 0 else s[-1]
            s.append(arr[i])
        return result

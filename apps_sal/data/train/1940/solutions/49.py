class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        stk = []
        i = 0
        while i < len(arr):
            while stk and arr[stk[-1]] < arr[i]:
                arr[stk.pop()] = arr[i]
            stk.append(i)
            i += 1
        while stk:
            arr[stk.pop()] = 0
        return arr

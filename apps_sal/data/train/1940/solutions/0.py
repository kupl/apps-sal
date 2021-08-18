class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head == None:
            return 0
        temp = head
        arr = []
        stack = []
        while temp:
            arr.append(temp.val)
            temp = temp.__next__
        output = [0] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                output[stack.pop()] = arr[i]
            stack.append(i)
        return output

class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        results = {}
        stack = deque()
        next = head.__next__
        curr = head
        extra_values = 0
        stack.append((0, curr.val))
        index = 0
        while next != None:
            while len(stack) != 0 and stack[-1][1] < next.val:
                (ind, val) = stack.pop()
                print((ind, val))
                results[ind] = next.val
            index += 1
            stack.append((index, next.val))
            next = next.__next__
        for i in range(len(stack)):
            results[stack[i][0]] = 0
        result_arr = [0] * len(results)
        for j in range(len(result_arr)):
            result_arr[j] = results[j]
        return result_arr

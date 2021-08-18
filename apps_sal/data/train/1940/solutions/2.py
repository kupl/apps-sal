class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        count_list = 0
        tmp = head
        while tmp:
            count_list += 1
            tmp = tmp.next
        result = [0] * count_list
        stack = list()
        position = 0
        while head:
            while len(stack) and stack[-1][0] < head.val:
                result[stack[-1][1]] = head.val
                stack.pop()
            stack.append((head.val, position))
            position += 1
            head = head.next

        return result

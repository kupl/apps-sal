# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerVal(self, in_list):
        length = len(in_list)
        i = length - 1

        stack = []
        answer = []

        while i >= 0:
            if not stack:
                answer.append(0)
            elif stack and stack[-1] > in_list[i]:
                answer.append(stack[-1])
            elif stack and stack[-1] <= in_list[i]:
                while stack and stack[-1] <= in_list[i]:
                    stack.pop()

                if stack:
                    answer.append(stack[-1])
                else:
                    answer.append(0)

            stack.append(in_list[i])
            i -= 1

        print(('Result is: {}'.format(answer[::-1])))
        return answer[::-1]

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head is None:
            return
        if head.__next__ is None:
            return [0]

        temp = head

        input_list = []

        while temp:
            input_list.append(temp.val)
            temp = temp.__next__

        result = self.nextLargerVal(input_list)

        return result

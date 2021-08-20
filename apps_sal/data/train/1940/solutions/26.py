class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        numbers = []
        answers = []
        while head:
            numbers.append(head.val)
            answers.append(0)
            head = head.next
            n = len(numbers) - 1
            while head and n >= 0 and (head.val > numbers[n]):
                if answers[n] == 0:
                    answers[n] = head.val
                n -= 1
        return answers

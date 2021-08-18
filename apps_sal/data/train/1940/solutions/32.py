class Solution:
    def __init__(self):
        self.result = []
        self.stack = []

    def nextLargerNodes(self, head: ListNode) -> list:
        self.__recursive(head)
        return self.result[::-1]

    def __recursive(self, head: ListNode) -> None:
        if head == None:
            return

        self.__recursive(head.__next__)

        val = 0
        while len(self.stack) != 0:
            val = self.stack.pop()

            if val > head.val:
                self.result.append(val)
                self.stack.extend([val, head.val])
                break

        if len(self.stack) == 0:
            self.result.append(0)
            self.stack.append(head.val)

        return

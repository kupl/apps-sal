class Solution:

    def find_best(self, head):
        current = head
        while current.next:
            if current.next.val > head.val:
                return current.next.val
            current = current.next
        return 0

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        self.lst = []

        def helper(head, i):
            if not head:
                return
            self.lst.append(0)
            helper(head.next, i + 1)
            if head.next:
                if head.next.val > head.val:
                    self.lst[i] = head.next.val
                elif self.lst[i + 1] == 0 or self.lst[i + 1] > head.val:
                    self.lst[i] = self.lst[i + 1]
                else:
                    self.lst[i] = self.find_best(head)
        helper(head, 0)
        return self.lst

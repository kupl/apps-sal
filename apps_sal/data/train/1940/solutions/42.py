class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.__next__
        stack = []
        res = [0 for _ in range(len(val_list))]
        for i in range(len(val_list)):
            while stack and val_list[stack[-1]] < val_list[i]:
                res[stack.pop()] = val_list[i]
            stack.append(i)
        return res

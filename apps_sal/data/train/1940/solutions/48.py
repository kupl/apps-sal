class Solution:

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        n = len(ans)
        lst = []
        for i in range(n - 1, -1, -1):
            v = ans[i]
            while lst and lst[-1] <= v:
                lst.pop()
            ans[i] = 0 if not lst else lst[-1]
            lst.append(v)
        return ans

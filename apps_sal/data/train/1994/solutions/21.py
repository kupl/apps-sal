class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        s = set(G)

        def func(head, path):
            nonlocal res
            if head:
                nonlocal s
                if head.val in s:
                    path.append(head.val)
                    s.remove(head.val)
                    func(head.next, path.copy())
                else:
                    if len(path):
                        res += 1
                    func(head.next, [])
            elif len(path):
                res += 1
        func(head, [])
        return res

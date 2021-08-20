class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        initial_c = len(G)
        runner = head
        ans = []
        conn_ll = []
        while runner:
            if runner.val in G:
                conn_ll.append(runner.val)
            elif conn_ll:
                ans.append(conn_ll[:])
                conn_ll = []
            runner = runner.next
        if conn_ll:
            ans.append(conn_ll)
        print(ans)
        return len(ans)

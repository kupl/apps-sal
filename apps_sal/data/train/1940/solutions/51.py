class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        st, res = [], [0] * len(arr)
        for i in range(len(arr)):
            while st and arr[i] > arr[st[-1]]:
                res[st.pop()] = arr[i]
            st.append(i)
        return res

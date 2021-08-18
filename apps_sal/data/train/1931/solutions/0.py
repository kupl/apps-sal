class Solution(object):
    def isSubPath(self, h, r0):
        h_vals = []
        while h:
            h_vals.append(str(h.val))
            h = h.next
        h_str = ('-'.join(h_vals)) + '-'

        st = [(r0, '-')]

        while st:
            r, pre = st.pop()
            if not r:
                continue

            pre = pre + str(r.val) + '-'
            if pre.endswith(h_str):
                return True

            st.append((r.left, pre))
            st.append((r.right, pre))

        return False

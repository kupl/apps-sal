class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = list(S)
        ud = 1
        while ud == 1:
            ud = 0
            i = 1
            while i <= len(st) - 1:
                if st[i] == st[i - 1]:
                    st.pop(i)
                    st.pop(i - 1)
                    ud = 1
                i += 1
        return ''.join(st)

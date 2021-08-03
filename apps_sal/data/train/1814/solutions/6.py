class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        dict = {}
        st = []
        ans = []
        for i in range(n):
            dict[i] = 0
        # print(dict)
        for s in logs:
            if s.split(':')[1] == 'start':
                if not st:
                    st.append([int(s.split(':')[0]), int(s.split(':')[2])])
                    # print(st)
                else:
                    time = int(s.split(':')[2]) - st[-1][1]
                    dict[st[-1][0]] += time
                    # print(dict)
                    st.append([int(s.split(':')[0]), int(s.split(':')[2])])
                    # print(st)
            else:
                time = int(s.split(':')[2]) - st[-1][1]
                dict[st[-1][0]] += time + 1
                # print(dict)
                st.pop()
                # print(st)
                if st:
                    st[-1][1] = int(s.split(':')[2]) + 1
                    # print(st)

        for i in range(n):
            ans += [dict[i]]

        return ans

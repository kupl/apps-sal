class Solution:

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        m1 = -1
        m = 0
        MA = 1
        dict = {-1: 0}
        for i in range(0, 4):
            for j in range(i + 1, 4):
                if i != j:
                    arr2 = deepcopy(arr)
                    del arr2[j]
                    del arr2[i]
                    a1 = arr2[0] + 10 * arr2[1]
                    a2 = arr2[1] + 10 * arr2[0]
                    if 1 > 0:
                        if a1 >= 60 and a2 >= 60:
                            MA = -1
                        elif a1 < 60 and a2 < 60:
                            m = max(a1, a2)
                            MA = 1
                        elif a1 < 60:
                            m = a1
                            MA = 1
                        elif a2 < 60:
                            m = a2
                            MA = 1
                    if MA == 1:
                        if 10 * arr[i] + arr[j] < 24 and 10 * arr[j] + arr[i] < 24:
                            if max(10 * arr[i] + arr[j], 10 * arr[j] + arr[i]) > m1:
                                m1 = max(10 * arr[i] + arr[j], 10 * arr[j] + arr[i])
                                dict[m1] = m
                            elif max(10 * arr[i] + arr[j], 10 * arr[j] + arr[i]) == m1:
                                if dict[m1] < m:
                                    dict[m1] = m
                        elif 10 * arr[i] + arr[j] < 24:
                            if 10 * arr[i] + arr[j] > m1:
                                m1 = 10 * arr[i] + arr[j]
                                dict[m1] = m
                            elif 10 * arr[i] + arr[j] == m1:
                                if dict[m1] < m:
                                    dict[m1] = m
                        elif 10 * arr[j] + arr[i] < 24:
                            if 10 * arr[j] + arr[i] > m1:
                                m1 = 10 * arr[j] + arr[i]
                                dict[m1] = m
                            elif 10 * arr[j] + arr[i] == m1:
                                if dict[m1] < m:
                                    dict[m1] = m
        if m1 == -1:
            return ''
        elif m1 // 10 == 0 and dict[m1] // 10 == 0:
            return '0' + str(m1) + ':0' + str(dict[m1])
        elif m1 // 10 == 0:
            return '0' + str(m1) + ':' + str(dict[m1])
        elif dict[m1] // 10 == 0:
            return str(m1) + ':0' + str(dict[m1])
        else:
            return str(m1) + ':' + str(dict[m1])

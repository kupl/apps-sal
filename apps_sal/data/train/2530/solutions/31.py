class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_noZero = sorted([i % 60 for i in time if i % 60 != 0])
        (i, j) = (0, len(time_noZero) - 1)
        m_60 = sorted([i % 60 for i in time if i % 60 == 0])
        count = int(len(m_60) * (len(m_60) - 1) / 2)
        while i < j:
            if time_noZero[i] + time_noZero[j] == 60:
                if time_noZero[i] != time_noZero[j]:
                    count += time_noZero.count(time_noZero[j]) * time_noZero.count(time_noZero[i])
                    l = time_noZero[i]
                    r = time_noZero[j]
                    while time_noZero[i] == l:
                        i += 1
                    while time_noZero[j] == r:
                        j -= 1
                else:
                    count += int(time_noZero.count(time_noZero[i]) * (time_noZero.count(time_noZero[i]) - 1) / 2)
                    break
            elif time_noZero[i] + time_noZero[j] < 60:
                i += 1
            else:
                j -= 1
        return count

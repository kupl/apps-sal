from collections import defaultdict


def time_diff(S1, S2):
    (h1, h2, m1, m2) = (int(S1[:2]), int(S2[:2]), int(S1[3:5]), int(S2[3:5]))
    h_diff = h2 - h1
    m_diff = m2 - m1
    return (h2 - h1) * 60 + m2 - m1


class Solution:

    def alertNames(self, keyName, keyTime):
        ans = set()
        names = defaultdict(list)
        time_name = sorted(list(zip(keyTime, keyName)))
        for (time, name) in time_name:
            names[name].append(time)
            if len(names[name]) >= 3 and time_diff(names[name][-3], names[name][-1]) <= 60:
                ans.add(name)
        print(names)
        return sorted(list(ans))

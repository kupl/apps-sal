class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        temp = []

        for name, time in zip(keyName, keyTime):
            temp.append([name, time])

        temp.sort(key=lambda x: (x[0], x[1]))

        ans = []

        def inhour(t1, t3):
            def hrmn(t1):
                hr, mn = t1.split(':')
                return int(hr) * 60 + int(mn)

            it1, it3 = hrmn(t1), hrmn(t3)

            return it3 - it1 <= 60

        for i in range(2, len(temp)):
            (name1, time1) = temp[i - 2]
            (name3, time3) = temp[i]
            if name1 == name3:
                if inhour(time1, time3) and (len(ans) == 0 or ans[-1] != name1):
                    ans.append(name1)

        return ans

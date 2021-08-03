import datetime


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def time_to_sec(time):
            [hours, minutes] = [int(x) for x in time.split(':')]
            x = datetime.timedelta(hours=hours, minutes=minutes)
            return x.seconds

        dic = {}

        sec = []
        for i in range(len(keyTime)):
            sec.append(time_to_sec(keyTime[i]))

        # name=[x for _, x in sorted(zip(sec, keyName), key=lambda pair: pair[0])]

        # print(name)
        name = keyName

        for i in range(len(name)):
            if name[i] not in dic:
                dic[name[i]] = [sec[i]]
            else:
                dic[name[i]].append(sec[i])

        for key, value in list(dic.items()):
            value.sort()
        # print(dic)
        ans = []
        for key, value in list(dic.items()):
            if len(value) >= 3:
                count = 1
                i = 0
                j = 1
                while j < len(value):
                    if value[j] - value[i] <= 3600:
                        if value[j] - value[i] != 0:
                            count += 1
                        j += 1
                    else:
                        i += 1
                        count = 1

                    if count == 3:
                        ans.append(key)
                    # print(count)
        return sorted(list(set(ans)))

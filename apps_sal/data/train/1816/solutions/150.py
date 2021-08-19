class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        keytime_table = dict()
        for idx in range(len(keyName)):
            name = keyName[idx]
            time = keyTime[idx]
            keytime_table.setdefault(name, []).append(time)

        ans = []
        for name in list(keytime_table.keys()):
            time_list = keytime_table[name]
            time_list.sort()
            l = 0
            r = 0
            hour, minute = time_list[0].split(':')
            l_minutes = int(hour) * 60 + int(minute)
            while l <= r and r < len(time_list):
                r_time = time_list[r]
                hour, minute = r_time.split(':')
                r_minutes = int(hour) * 60 + int(minute)
                #print(l, r, name, time_list, l_minutes, r_minutes, ans)
                if r_minutes - l_minutes <= 60:
                    if r - l >= 2:
                        ans.append(name)
                        break
                    r += 1
                else:
                    l += 1
                    if l > r:
                        r += 1
                    l_time = time_list[l]
                    hour, minute = l_time.split(':')
                    l_minutes = int(hour) * 60 + int(minute)
        ans.sort()
        return ans

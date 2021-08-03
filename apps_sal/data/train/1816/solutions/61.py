from functools import cmp_to_key


def cmp(a, b):
    if(a[1] > b[1]):
        return 1
    return -1


def secs(time):
    hr, mins = time.split(':')
    s = int(hr) * 3600 + int(mins) * 60
    return s


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        N = len(keyName)
        l = []
        for i in range(N):
            l.append([keyName[i], keyTime[i]])
        l.sort(key=cmp_to_key(cmp))
        d = {}
        s = set()

        for name, time in l:
            if(name in s):
                continue
            if(name not in d):
                d[name] = [secs(time)]
            else:
                i = 0
                curr_time = secs(time)
                while(i < len(d[name]) and curr_time - d[name][i] > 3600):
                    i += 1

                d[name] = d[name][i:] + [curr_time]
                if(len(d[name]) >= 3):
                    s.add(name)
        return sorted(list(s))

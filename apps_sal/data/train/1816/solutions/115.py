class Solution:

    def alertNames(self, name: List[str], time: List[str]) -> List[str]:
        n = len(time)
        arr = []
        mapper = {}
        for i in range(n):
            (hr, mm) = list(map(int, time[i].split(':')))
            time_in_min = hr * 60 + mm
            worker = name[i]
            if worker in mapper:
                mapper[worker].append(time_in_min)
            else:
                mapper[worker] = [time_in_min]
        for i in mapper:
            value = mapper[i]
            value.sort()
            mapper[i] = value
        for i in mapper:
            value = mapper[i]
            if len(value) >= 3:
                st = 0
                en = 2
                while en < len(value):
                    if value[en] - value[st] <= 60:
                        arr.append(i)
                        break
                    en += 1
                    st += 1
        if arr == []:
            return []
        arr.sort()
        return arr

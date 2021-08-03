class Solution:
    def alertNames(self, name: List[str], time: List[str]) -> List[str]:
        # number of cases in array.
        n = len(time)

        # array which contains name of workers who received an alert.
        arr = []

        # map which contains name as key and list of times(in minutes) as value.
        mapper = {}

        for i in range(n):
            hr, mm = list(map(int, time[i].split(':')))
            # finding time in minutes
            time_in_min = hr * 60 + mm
            worker = name[i]
            if worker in mapper:
                mapper[worker].append(time_in_min)
            else:
                mapper[worker] = [time_in_min]

        # sorting the list(sorting time for each worker) of all keys in mapper
        for i in mapper:
            value = mapper[i]
            value.sort()
            mapper[i] = value

        for i in mapper:
            value = mapper[i]
            # possiblity of getting use of card 3 or more than 3 times
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
        # sorting names in alphabetical order.
        arr.sort()
        return arr

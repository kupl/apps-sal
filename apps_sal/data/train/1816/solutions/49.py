class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        '''
        mapping ={
            'leslie': {
                '13' : 3,
                '14' : ['14:00', '14:45'],
                }
            }
        '''

        def to_ts(t: str):
            hour, minute = t.split(':')
            return 60 * int(hour) + int(minute)

        def in_a_hour(t1, t2):
            return abs(to_ts(t1) - to_ts(t2)) <= 60

        from datetime import datetime

        mapping = {name: [] for name in keyName}

        for i in range(len(keyName)):
            mapping[keyName[i]].append(keyTime[i])

        for val in list(mapping.values()):
            val.sort(key=to_ts)

        print(mapping)

        def more_than_3_in_a_hour(arr):
            l = r = 0
            while r < len(arr):
                if in_a_hour(arr[l], arr[r]):
                    if r - l >= 2:
                        return True
                    r += 1
                else:
                    l += 1

        return sorted([name for name, times in list(mapping.items()) if more_than_3_in_a_hour(times)])

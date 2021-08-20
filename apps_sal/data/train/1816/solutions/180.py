class Solution:

    def alertNames(self, keyName: 'List[str]', keyTime: 'List[str]') -> 'List[str]':
        N = len(keyName)
        arr = []
        for i in range(N):
            t = int(keyTime[i][:2]) * 60 + int(keyTime[i][3:])
            arr.append([t, keyName[i]])
        arr.sort()
        i = 0
        counter = collections.Counter()
        res = set()
        for j in range(N):
            while arr[j][0] - arr[i][0] > 60:
                counter[arr[i][1]] -= 1
                i += 1
            counter[arr[j][1]] += 1
            if counter[arr[j][1]] >= 3:
                res.add(arr[j][1])
        return sorted(list(res))

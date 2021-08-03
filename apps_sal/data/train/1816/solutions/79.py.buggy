class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def getNumMins(time):
            time = time.split(\":\")
            hours = int(time[0])
            mins = int(time[1])
            return (hours * 60) + mins
        
        arr = []
        for i in range(len(keyName)):
            arr.append((getNumMins(keyTime[i]), keyName[i]))
        arr.sort()
        print(arr)
        
        access = collections.defaultdict(list)
        for time, key in arr:
            access[key].append(time)
        
        res = []
        for key in sorted(access.keys()):
            times = access[key]
            for i in range(len(times) - 3 + 1):
                if (times[i+2] - times[i]) <= 60:
                    res.append(key)
                    break
        
        return res
    

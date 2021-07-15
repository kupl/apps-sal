class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        worker_dict = {}
        for i in range(len(keyName)):
            worker = keyName[i]
            time = keyTime[i]
            if worker in worker_dict:
                worker_dict[worker].append(time)
            else:
                worker_dict[worker] = [time]
        ret = [worker for worker in worker_dict.keys() if self.three_or_more(worker_dict[worker])]
        return sorted(ret)
    
    def three_or_more(self, times):
        times = sorted(times)
        for i in range(len(times)):
            count = 0
            time = times[i]
            within_hour_curr = [times[j] for j in range(i, len(times)) if self.within_hour(time, times[j])]
            if len(within_hour_curr) >= 3:
                return True
        return False
    
    def within_hour(self, time1, time2):
        earlier = min(time1, time2)
        later = max(time1, time2)
        e_hour, e_min = earlier.split(\":\")
        l_hour, l_min = later.split(\":\")
        if l_hour == e_hour:
            return True
        elif int(l_hour) - int(e_hour) == 1:
            if int(l_min) <= int(e_min):
                return True
        return False
            

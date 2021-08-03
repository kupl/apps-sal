class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        visit_times = {}
        ans = set()
        for i, name in enumerate(keyName):
            visit_times[name]= visit_times.get(name,[]) + [keyTime[i]]
        for employee in visit_times.keys():
            visit_times[employee] = sorted(visit_times[employee])
            for i in range(len(visit_times[employee])-2):
                if not(self.hour_diff(visit_times[employee][i],visit_times[employee][i+2])):
                    ans.add(employee)
        return sorted(list(ans))
                
        
    def hour_diff(self, a,b):
        minute_a = int(a.split(\":\")[1])
        minute_b = int(b.split(\":\")[1])
        hour_a = int(a.split(\":\")[0])
        hour_b = int(b.split(\":\")[0])
        minute_diff = minute_b-minute_a
        hour_diff = hour_b-hour_a
        return (hour_diff > 1 or (hour_diff == 1 and minute_diff>0)) or hour_diff < 0

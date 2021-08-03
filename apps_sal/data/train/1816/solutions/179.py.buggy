class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def to_minutes(t: str) -> int:
            assert len(t) == 5
            assert t[2] == \":\"
            return int(t[0:2]) * 60 + int(t[3:5])
        
        def from_minutes(mins: int) -> str:
            return \"{:02d}:{:02d}\".format((mins - mins % 60) // 60, mins % 60)

        # return true if : t1 < t2
        def compare_times(t1: str, t2: str) -> bool:
            return to_minutes(t1) < to_minutes(t2)
            
        def add_hours(t: str, hours: int) -> str:
            return from_minutes(60 * hours + to_minutes(t))
                
        lookup = {}
        
        output = set()
        for name, time in zip(keyName, keyTime):
            if name in lookup:
                lookup[name].append(time)
            else:
                lookup[name] = [time]
        for name in lookup:
            lookup[name].sort()
            times = []
            for time in lookup[name]:
                while times and compare_times(add_hours(times[0], 1), time):
                    times.pop(0)
                times.append(time)
                if len(times) >= 3:
                    output.add(name)
                
        return sorted(list(output))

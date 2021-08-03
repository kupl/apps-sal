class Solution:
    def alertNames(self, key_names: List[str], key_times: List[str]) -> List[str]:
        
        def timestamp(time):
            h, m = time.split(\":\")
            return 60 * int(h) + int(m)
            
        alerted = set() #names that have already been alerted
        recent = defaultdict(deque) #name : recent timestamps, in  order
        
        #sort by timestamp
        for time, name in sorted(zip((timestamp(t) for t in key_times), key_names)):
            if name not in alerted:
                recent[name].append(time)
                while recent[name] and recent[name][0] < time - 60:
                    recent[name].popleft()
                if len(recent[name]) >= 3:
                    alerted.add(name)
                    recent.pop(name)
        
        return sorted(alerted)

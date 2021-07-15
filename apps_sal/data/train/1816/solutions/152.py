class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import defaultdict
        
        key_pairs = [(time, name) for name, time in zip(keyName, keyTime)]
        key_pairs.sort()
        keys = defaultdict(list)
        names = set()
        for pair in key_pairs:
            time, name = pair
            if name in names:
                continue
                
            keys[name].append(time)
            
            if len(keys[name]) < 3:
                continue
            
            hour, minute = time.split(':')
            hour, minute = int(hour), int(minute)
            first_access_time = keys[name][-3]
            first_hour, first_minute = first_access_time.split(':')
            first_hour, first_minute = int(first_hour), int(first_minute)
            if hour - first_hour <= 1:
                if hour - first_hour == 1:
                    if minute - first_minute > 0:
                        continue
                    else:
                        names.add(name)
                else:
                    names.add(name)
        res = list(names)
        res.sort()
        
        return res

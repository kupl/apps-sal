class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        events = collections.defaultdict(list)
        for name, time in sorted(zip(keyName, keyTime)):
            h, m = time.split(\":\")
            h, m = int(h), int(m)
            events[name].append(h*60+m)
        
        alert = []
        for name in events:
            T = events[name]
            n = len(T)
            left, right = 0, 0
            while right < n:
                r = T[right]
                right += 1
                
                while r-T[left] > 60:
                    left += 1
                    
                if right - left >= 3:
                    alert.append(name)
                    break
        return alert            

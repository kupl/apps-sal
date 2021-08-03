from collections import defaultdict, deque

class Solution:
    def alertNames(self, name: List[str], time: List[str]) -> List[str]:
        z = zip(name, time)
        hmap = defaultdict(list)
        for c in z:
            h, m = map(int,c[1].split(\":\"))
            t = h *60 + m
            hmap[c[0]].append(t)
        print(hmap)
        
        names, op = list(set(name)), []
        names.sort()
                
        for name in names:
            hmap[name].sort() 
            found = False
            current = deque()
            
            for time in hmap[name]:
                current.append(time)
                while time - current[0] > 60:
                    current.popleft()
                found |= len(current) >= 3
            if found:
                op.append(name)
        
        return op

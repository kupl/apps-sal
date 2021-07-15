class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        m = collections.defaultdict(set)
        for n, t in zip(keyName, keyTime):
            m[n].add(t)
            
        ans = []
        # print(m)
        
        for name in m:
            added = False
            times = m[name]
            m2 = collections.defaultdict(set)
            for t in times:
                h, minute = map(int, t.split(':'))
                m2[h].add(minute)
                
            # print(name, m2)
            for h, f in m2.items():
                if len(f) >= 3:
                    ans.append(name)
                    added = True
                    break
                
            if added:  # name is already added
                continue
                
            to_minutes = []
            for t in times:
                h, minute = map(int, t.split(':'))
                to_minutes.append(h * 60 + minute)
            to_minutes.sort()
            # print(name, to_minutes)
            i = 0
            j = 0
            size = 1
            while i < len(to_minutes) and j < len(to_minutes) - 1:
                if to_minutes[j + 1] - to_minutes[i] <= 60:
                    j += 1
                    if j - i >= 2:
                        # print(to_minutes[i])
                        ans.append(name)
                        break
                else:
                    i += 1
                    # size -= 1
                j = max(j, i)
            
        
        return sorted(ans)

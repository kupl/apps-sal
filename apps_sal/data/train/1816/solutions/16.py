class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        
        alert = defaultdict(dict)
        ans = []
        zipper = list(zip(keyName, keyTime))
        zipper = list(zipper)
        zipper.sort(key = lambda x: (x[0], x[1]))
        
        for i in range(n - 2):
            (name, time) = zipper[i]
            if name in ans:
                continue
            (next_name, next_time) = zipper[i + 2]
            
            if next_name != name:
                continue
                
            time = int(time[:2] + time[3:])
            next_time = int(next_time[:2] + next_time[3:])
            
            if next_time - time <= 100:
                ans.append(name)
                
        return ans


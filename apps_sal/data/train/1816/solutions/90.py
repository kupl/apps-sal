from datetime import timedelta 


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dp = defaultdict(list) 
        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i]
            dp[name].append(time)
        
        def check(ls):
            ls = sorted(ls)
            start, end = 0, 0
            # guarantee safe access on arr
            make_date = lambda x: timedelta(hours = int(x[:2]), minutes = int(x[3:]))
            
            
            def outer_check(start, end): 
                return (make_date(end) - make_date(start)).total_seconds() <= 3600 and int(start[:2]) - int(end[:2]) < 24
            
            while end < len(ls) and start <= end: 
                while end < len(ls) and outer_check(ls[start], ls[end]):
                    end += 1
                if (end - start) >= 3:
                      return True
                start += 1 
            return False
        
        res = []
                      
        for name, t in list(dp.items()):
            if check(t):
                res.append(name)
        return sorted(res)


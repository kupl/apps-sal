class Solution:
    def alertNames(self, names: List[str], times: List[str]) -> List[str]:
        dic = {}
        n = len(names)
        alert = set()
        
        arr = [tup for tup in zip(names, times)]
        
        arr.sort(key = lambda ele: ele[1])
        
        for i in range(n):
            name, time = arr[i][0], arr[i][1]
            tup = time.split(':')
            hour, minu = int(tup[0]), int(tup[1])
            int_time = hour * 60 + minu
            dic[name] = dic.get(name, []) + [int_time]
            
            curlen = len(dic[name])
            if curlen >= 3 and int_time - dic[name][curlen-3] <= 60:
                alert.add(name)
                
        return sorted(list(alert))
        
            
            


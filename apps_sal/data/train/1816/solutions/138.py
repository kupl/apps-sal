def time2num(t):
    h,m = t.split(':')
    # print(h,m)
    return [int(h), int(m)]

def check_1hour(t1, t2):
    if t1[0] == t2[0]:
        return True
    if t2[0]-t1[0] ==1 and t2[1]<=t1[1]:
        return True
    return False

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        dt = {}
        for k, v in zip(keyName, keyTime):
            if k in dt:
                dt[k].append(v)
            else:
                dt[k] = [v]
        res = []
        for k, v in list(dt.items()):
            if len(v) < 3:
                continue
            if Solution.find_time(v):
                res.append(k)
        
        return sorted(res)
    
    @staticmethod
    def find_time(list_time):
        l2 = list(map(time2num, list_time))
        print(l2)
        l2 = sorted(l2)    
        # print(l2)
        # print(list_time)
        n = len(list_time)        
        for i in range(n-2):
            if check_1hour(l2[i], l2[i+2]):
                return True
        return False
            
            
        


from sortedcontainers import SortedList
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hm = defaultdict(SortedList)
        res = set()
        
        for name, time in zip(keyName, keyTime):
            int_time = self.get_time_as_int(time)
            hm[name].add(int_time)

        for name in hm:
            if self.check(hm[name]):
                res.add(name)
        return sorted(res)
    
    def check(self, arr):
        left = 0
        for right in range(len(arr)):
            if right - left + 1 == 3:
                if arr[right] - arr[left] <= 100:
                    return True
                left += 1
        return False
    
    def get_time_as_int(self, time):
        t1 = time[:2]
        t2 = time[3:]
        int_time = int(t1+t2)
        return int_time


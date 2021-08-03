class Solution:
    
    def getTimeInMinutes(self, time):
        hour,minute = time.split(\":\")
        hour = int(hour)
        minute = int(minute)
        return hour * 60 + minute
    
    def alert(self, swipeTimes):
        window = collections.deque()
        for time in swipeTimes:
            while len(window) > 0 and time - window[0] > 60:
                window.popleft()
            window.append(time)
            if len(window) >= 3:
                return True
        return False
     
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        swipes = collections.defaultdict(list)
        for index in range(len(keyName)):
            swipes[keyName[index]].append(self.getTimeInMinutes(keyTime[index]))
            
        result = []
        for key in swipes:
            swipes[key].sort()
            if self.alert(swipes[key]):
                result.append(key)
        
        result.sort()
        return result

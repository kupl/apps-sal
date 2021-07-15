class TweetCounts:

    def __init__(self):
        self.map = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.map:
            self.map[tweetName].append(time)
        else:
            self.map[tweetName] = [time] 

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        if freq == \"minute\": seconds = 60 
        elif freq == \"hour\": seconds = 3600
        else: seconds = 86400
        
        ans = [0] * ((endTime - startTime)//seconds + 1)
        for t in self.map[tweetName]:
            if startTime <= t <= endTime: ans[(t-startTime)//seconds] += 1
        return ans 
        
#         times = self.map[tweetName]
        
#         size = 0 
#         delta = 0
        
#         if(freq == 'minute'):
#             delta = 60
#             size = (endTime - startTime) / delta + 1
#         if(freq == 'hour'):
#             delta = 3600
#             size = (endTime - startTime) / delta + 1
#         if(freq == 'day'):
#             delta = 86400
#             size = (endTime - startTime) / delta + 1
                
#         r = [0] * int(size)
        
#         for i in times:
#             if(startTime <= i and i <= endTime):
#                 index = int((i-startTime)/delta)
#                 r[index] += 1

#         return r  
    
    

#         delta = 0
#         if freq == \"minute\": 
#             delta = 60
#         elif freq == \"hour\":
#             delta = 3600
#         else:
#             delta =60*60*24
        
#         #value list
#         self.map[tweetName].sort()
#         tweetTimes = self.map[tweetName]
        
        
#         size = (endTime-startTime)//delta+1
#         res = [0]*size
             
#         #for loop that goes through time intervals and counts # of tweets in that interval
#         startRange = 0
#         endRange = 0
#         secs = delta
#         for i in range(0, (size)):
#             startRange = startTime + delta*i
#             endRange = min(startTime + delta*(i+1), endTime+1)

#             for tweetTime in tweetTimes:
#                 if tweetTime >= endRange:
#                     break
#                 if tweetTime >= startRange and tweetTime < endRange:
#                     index = int((tweetTime-startTime)/secs)
#                     res[index] +=1
            
#         return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

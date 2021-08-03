import numpy as np

class TweetCounts:

    def __init__(self):
        self.tweets = {}
        self.tweets_sorted = {}
        self.intervals = {\"minute\": 60, \"hour\": 3600, \"day\": 3600 * 24}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        if not tweetName in self.tweets: 
            self.tweets[tweetName] = np.array([])
        
        self.tweets_sorted[tweetName] = False
        self.tweets[tweetName] = np.append(self.tweets[tweetName], [time])
        # print(self.tweets[tweetName])
        

#     def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
#         interval = self.intervals[freq]
#         # bins = [[i*interval, (i+1)*interval] for i in range(int(np.ceil((endTime - startTime) / interval)))]
#         bins = []
#         t_start=startTime
#         while t_start <= endTime:
#             bins.append([t_start, t_start + interval])
#             t_start += interval
        
#         bins[-1][1] = endTime + 1
        
#         # h,e = np.histogram(self.tweets[tweetName], bins=interval, range=(startTime, endTime))
#         count = np.zeros(len(bins), dtype=np.int)
        
#         for t in self.tweets[tweetName]:
#             for bi, b in enumerate(bins):
#                 if b[0]<= t < b[1]:
#                     count[bi] += 1
                    
#         return h 

    
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = self.intervals[freq]
        # bins = [[i*interval, (i+1)*interval] for i in range(int(np.ceil((endTime - startTime) / interval)))]
        bins = []
        t_start=startTime
        while t_start <= endTime:
            bins.append([t_start, t_start + interval])
            t_start += interval
        
        bins[-1][1] = endTime + 1
        count = np.zeros(len(bins), dtype=np.int)
        
        if not self.tweets_sorted[tweetName]: self.tweets[tweetName].sort()
        
        e_end = startTime + interval
        
        ## Find borders
        i_start, i_end = np.searchsorted(self.tweets[tweetName], v=[startTime-1, endTime+1], side=\"right\")
        int_i = 0
        for t in self.tweets[tweetName][i_start:i_end]:
            while t >= e_end and t <= endTime:
                int_i += 1
                e_end += interval
            
            if t <= endTime: count[int_i] += 1       
                    
        return count    


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

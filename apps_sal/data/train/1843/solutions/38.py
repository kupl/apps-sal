class TweetCounts:

    def __init__(self):
        self.tweets = {}
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in list(self.tweets.keys()):
            bisect.insort(self.tweets[tweetName], time)
        else:
            self.tweets[tweetName] = [time]
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets:
            return []
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400 
        time_list = self.tweets[tweetName]
        
        size = int((endTime-startTime)//delta) +1
        res = [0]*size
        for t in time_list:
            if startTime <= t <= endTime:
                index = int((t-startTime)//delta)
                res[index] += 1        
        
        # i = delta
        # if len(time_list) == 1:
        #     if time_list[0] < startTime or time_list[0] > endTime:
        #         res.append([0]*size)
        #         return res[0]
        # while startTime <= endTime:
        #     while i < startTime:
        #         i+=delta
        #     count = 0
        #     for t in time_list:
        #         if startTime <= t <i:
        #             count += 1
        #     res.append(count)
        #     startTime += delta
        #     i += delta
        return res
    

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)


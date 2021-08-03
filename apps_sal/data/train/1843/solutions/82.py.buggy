class TweetCounts:

    def __init__(self):
        self.tweets = {}
        
        self.delta = {\"minute\": 60, \"hour\": 3600, \"day\": 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweets:
            self.tweets[tweetName].append(time)
        else:
            self.tweets[tweetName] = [time]
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        times = sorted(filter(lambda t: startTime <= t <= endTime, self.tweets.get(tweetName, [])))
        
        delta = self.delta[freq]
        
        ranges = [[startTime + delta*i, startTime + delta*(i+1)-1] \\
                  for i in range((endTime - startTime) // delta)]
        
        ranges.append([startTime + delta*len(ranges), endTime])
        
        counts = {tuple(k): 0 for k in ranges}
        
        i = 0
        for n in times:
            while n > ranges[i][1]:
                i += 1
                
            counts[tuple(ranges[i])] += 1
            
        
        return counts.values()
            
                       
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

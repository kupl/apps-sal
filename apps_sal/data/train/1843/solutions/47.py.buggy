from collections import defaultdict


class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        times = self.tweets[tweetName]
        length = endTime - startTime
        
        if freq == \"minute\":
            units = 60
        elif freq == \"hour\":
            units = 3600
        else:
            units = 3600 * 24
            
        intervals = {}
        i = 0
        for _ in range(startTime, endTime + 1, units):
            intervals[i] = 0
            i += 1
            
        for t in times:
            if startTime <= t <= endTime:
                interval = (t - startTime) // units
                intervals[interval] += 1
                
        return list(intervals.values())


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

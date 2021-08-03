class TweetCounts:

    def __init__(self):
        self.records = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.records[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        record = self.records[tweetName]
        dt = 60
        if freq == \"hour\":
            dt *= 60
        elif freq == \"day\":
            dt *= 60 * 24
        res = [0] * ((endTime-startTime) // dt + 1)
        
        for t in record:
            if startTime <= t <= endTime:
                idx = (t - startTime) // dt
                res[idx] += 1
        return res

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

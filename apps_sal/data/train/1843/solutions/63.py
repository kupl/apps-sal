class TweetCounts:

    def __init__(self):
        self.lookup = collections.defaultdict(list)
        self.convert = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.lookup[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        seconds = self.convert[freq]
        ans = [0] * ((endTime - startTime) // seconds + 1)
        for time in self.lookup[tweetName]:
            if startTime <= time <= endTime:
                ans[(time - startTime) // seconds] += 1

        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

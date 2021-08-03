class TweetCounts:

    def __init__(self):
        self.data = collections.defaultdict(dict)

    def recordTweet(self, tweetName: str, time: int) -> None:
        if time not in self.data[tweetName]:
            self.data[tweetName][time] = 1
        else:
            self.data[tweetName][time] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = [60, 60 * 60, 60 * 60 * 24]
        if freq == 'minute':
            t = delta[0]
        elif freq == 'hour':
            t = delta[1]
        else:
            t = delta[2]
        res = [0] * ((endTime - startTime) // t + 1)
        i = 0
        data = self.data[tweetName]
        for time in sorted(data.keys()):
            if startTime <= time <= endTime:
                res[(time - startTime) // t] += data[time]
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

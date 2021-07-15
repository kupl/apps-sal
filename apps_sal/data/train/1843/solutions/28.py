class TweetCounts:

    def __init__(self):
        self.recorder = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.recorder[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        res, i, start = [], 1, startTime
        while start <= endTime:
            end = min(startTime + delta * i, endTime + 1)
            res.append(bisect_left(self.recorder[tweetName], end) - bisect_left(self.recorder[tweetName], start))
            start, i = end, i + 1
        return res
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)


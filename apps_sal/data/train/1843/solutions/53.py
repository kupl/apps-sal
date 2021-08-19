class TweetCounts:

    def __init__(self):
        self.d = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.d:
            self.d[tweetName] = [time]
        else:
            self.d[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            s = 60
        elif freq == 'hour':
            s = 3600
        else:
            s = 3600 * 24
        intervals = (endTime - startTime) // s + 1
        res = [0] * intervals
        times = self.d[tweetName]
        for t in times:
            if startTime <= t <= endTime:
                i = (t - startTime) // s
                res[i] += 1
        return res

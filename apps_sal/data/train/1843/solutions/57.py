class TweetCounts:

    def __init__(self):
        self.tw = collections.defaultdict(list)
        self.duration = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if not self.tw[tweetName]:
            self.tw[tweetName].append(time)
        else:
            ind = bisect.bisect(self.tw[tweetName], time)
            self.tw[tweetName] = self.tw[tweetName][:ind] + [time] + self.tw[tweetName][ind:]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        res = []
        q = self.tw[tweetName]
        s = startTime
        while s <= endTime:
            e = min(endTime, s + self.duration[freq] - 1)
            ind1 = bisect.bisect_left(q, s)
            ind2 = bisect.bisect_right(q, e, lo=ind1)
            res.append(ind2 - ind1)
            s = e + 1
        return res

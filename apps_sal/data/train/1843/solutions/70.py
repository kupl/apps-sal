import bisect


class TweetCounts:

    def __init__(self):
        self.td = dict()
        self.incrDict = {'minute': 60, 'hour': 60 * 60, 'day': 24 * 60 * 60}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.td[tweetName] = self.td.get(tweetName, list())
        self.td[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.td:
            return []
        tl = sorted(self.td.get(tweetName, list()))
        si = bisect.bisect_left(tl, startTime)
        ei = bisect.bisect_right(tl, endTime)
        incr = self.incrDict[freq]
        res = []
        for i in range(math.ceil((endTime - startTime + 1) / incr)):
            et = startTime + (i + 1) * incr
            ind = bisect.bisect_right(tl, et - 1, si, ei)
            res.append(ind - si)
            si = ind

        return res

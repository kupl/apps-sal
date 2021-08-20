class TweetCounts:
    FREQUENCE = {'minute': 60, 'hour': 3600, 'day': 24 * 3600}

    def __init__(self):
        self.store = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.store:
            self.store[tweetName] = {}
        if time not in self.store[tweetName]:
            self.store[tweetName][time] = 0
        self.store[tweetName][time] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.store:
            return []
        delta = TweetCounts.FREQUENCE[freq]
        keys = list(self.store.get(tweetName).keys())
        keys = sorted(keys)
        start = bisect.bisect_left(keys, startTime)
        end = bisect.bisect_right(keys, endTime)
        num_intervals = (endTime - startTime) // delta + 1
        result = [0] * num_intervals
        for t1 in range(start - 1, end + 1):
            if t1 < 0:
                continue
            if t1 >= len(keys):
                break
            t = keys[t1]
            if t < startTime or t > endTime:
                continue
            index = (t - startTime) // delta
            result[index] += self.store.get(tweetName).get(t)
        return result

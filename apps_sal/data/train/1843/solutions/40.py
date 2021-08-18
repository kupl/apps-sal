from collections import defaultdict
from bisect import insort, bisect_left


class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.d = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        record = self.tweets[tweetName]
        delta = self.d[freq]
        res = [0] * ((endTime - startTime) // delta + 1)
        for time in record:
            if time < startTime or time > endTime:
                continue
            res[(time - startTime) // delta] += 1
        return res

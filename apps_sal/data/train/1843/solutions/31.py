import bisect
from collections import defaultdict


class TweetCounts:

    def __init__(self):
        self._tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self._tweets[tweetName].insert(bisect.bisect_left(self._tweets[tweetName], time), time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        result = []
        while startTime <= endTime:
            end = min(startTime + delta, endTime + 1)
            result.append(bisect.bisect_left(self._tweets[tweetName], end) - bisect.bisect_left(self._tweets[tweetName], startTime))
            startTime += delta
        return result

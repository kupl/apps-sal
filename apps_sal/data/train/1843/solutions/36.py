class TweetCounts:
    FREQUENCEY_TO_SECONDS = {'minute': 60, 'hour': 3600, 'day': 86400}

    def __init__(self):
        self._data = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self._data[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = self.FREQUENCEY_TO_SECONDS.get(freq, None)
        if not delta:
            return []
        (i, result) = (startTime, [])
        while i <= endTime:
            j = min(i + delta, endTime + 1)
            left = bisect.bisect_left(self._data[tweetName], j)
            right = bisect.bisect_left(self._data[tweetName], i)
            result.append(left - right)
            i += delta
        return result

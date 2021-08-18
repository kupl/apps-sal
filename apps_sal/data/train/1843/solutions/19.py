class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = 60
        if freq == 'hour':
            delta = 3600
        elif freq == 'day':
            delta = 86400

        pre = bisect_left(self.tweets[tweetName], startTime)
        n = (endTime + 1 - startTime) // delta + (1 if (endTime + 1 - startTime) % delta != 0 else 0)
        end, res = startTime, []
        for _ in range(n):
            end = min(end + delta, endTime + 1)
            i = bisect_left(self.tweets[tweetName], end)
            res.append(i - pre)
            pre = i
        return res

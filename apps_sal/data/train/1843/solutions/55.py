class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        count = 0
        den = 0
        size = 0
        if freq == 'minute':
            den = 60
            size = (endTime - startTime) // 60 + 1
        elif freq == 'hour':
            den = 3600
            size = (endTime - startTime) // 3600 + 1
        else:
            den = 86400
            size = (endTime - startTime) // 86400 + 1
        op = [0] * size

        for t in self.tweets[tweetName]:
            if(startTime <= t and t <= endTime):
                idx = (t - startTime) // den
                op[idx] += 1

        return op

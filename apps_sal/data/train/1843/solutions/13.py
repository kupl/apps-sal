class TweetCounts:

    FREQUENCE = {
        'minute': 60,
        'hour': 3600,
        'day': 24 * 3600,
    }

    def __init__(self):
        self.tweets_dict = {}

    def recordTweet(self, tweetName: str, time: int) -> None:

        if tweetName not in self.tweets_dict:
            self.tweets_dict[tweetName] = []

        bisect.insort(self.tweets_dict.get(tweetName), time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:

        if tweetName not in self.tweets_dict:
            return []

        delta = TweetCounts.FREQUENCE[freq]

        num_intervals = (endTime - startTime) // delta + 1

        result = [0] * num_intervals

        for t in self.tweets_dict[tweetName]:
            if t < startTime:
                continue
            if t > endTime:
                break

            index = (t - startTime) // delta
            result[index] += 1

        return result

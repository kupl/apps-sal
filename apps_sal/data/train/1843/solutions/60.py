class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.setdefault(tweetName, {}).setdefault(time, 0)
        self.tweets[tweetName][time] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        eligible = []

        for (time, count) in list(self.tweets.get(tweetName, {}).items()):
            if startTime <= time <= endTime:
                eligible.append((time, count))

        if 'minute' == freq:
            samples = 60
        elif 'hour' == freq:
            samples = 3600
        elif 'day' == freq:
            samples = 86400
        else:
            raise RuntimeError(freq)

        num_results = 1 + ((endTime - startTime) // samples)
        results = [0] * num_results

        for (time, count) in eligible:
            offset = (time - startTime)
            if 'minute' == freq:
                offset //= 60
            elif 'hour' == freq:
                offset //= 3600
            elif 'day' == freq:
                offset //= 86400
            results[offset] += count
        return results

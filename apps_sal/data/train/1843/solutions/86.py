class TweetCounts:
    STEP_DICT = {
        \"minute\": 60,
        \"hour\": 60 * 60,
        \"day\": 60 * 60 * 24,
    }

    def __init__(self):
        self.tweet_map = defaultdict(list)

    def recordTweet(self, tweet_name: str, t: int) -> None:
        self.tweet_map[tweet_name].append(t)

    def getTweetCountsPerFrequency(self, freq: str, tweet_name: str, start: int, stop: int) -> List[int]:
        result = []

        if tweet_name not in self.tweet_map:
            return result

        step = self.STEP_DICT[freq]

        tweet_times = sorted([t for t in self.tweet_map[tweet_name] if start <= t <= stop])
        tweet_times_intervals = [(t - start) // step + 1 for t in tweet_times]
        tweet_times_intervals_dict = defaultdict(int)
        for interval in tweet_times_intervals:
            tweet_times_intervals_dict[interval] += 1

        interval = 1
        while start <= stop:
            result.append(tweet_times_intervals_dict.get(interval, 0))
            interval += 1
            start += step

        return result


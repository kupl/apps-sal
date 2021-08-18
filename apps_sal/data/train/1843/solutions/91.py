from collections import defaultdict
import bisect


class TweetCounts:

    freq_map = {'minute': 60, 'hour': 3600, 'day': 3600 * 24}

    def __init__(self):
        self.tweet_map = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweet_map[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:

        interval_length = TweetCounts.freq_map[freq]
        starting_index = bisect.bisect_left(self.tweet_map[tweetName], startTime)

        res = []
        curr_index = starting_index
        current_interval_start = startTime
        current_interval_end = min(current_interval_start + interval_length - 1, endTime)
        current_interval_count = 0
        while current_interval_end <= endTime:
            if curr_index < len(self.tweet_map[tweetName]):
                if self.tweet_map[tweetName][curr_index] <= current_interval_end:
                    current_interval_count += 1
                    curr_index += 1
                    continue
            if current_interval_end != endTime:
                current_interval_start += interval_length
                current_interval_end = min(current_interval_end + interval_length, endTime)
                res.append(current_interval_count)
                current_interval_count = 0
            else:
                res.append(current_interval_count)
                break

        return res

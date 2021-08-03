from collections import defaultdict
import bisect


class TweetCounts:

    freq_map = {'minute': 60, 'hour': 3600, 'day': 3600 * 24}

    def __init__(self):
        # map of tweetName => [] ordered list of frequencies
        self.tweet_map = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweet_map[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        # print(f'getTweetCountsPerFrequency: {startTime}: {endTime}: {freq}')

        interval_length = TweetCounts.freq_map[freq]
        # print(self.tweet_map[tweetName])
        starting_index = bisect.bisect_left(self.tweet_map[tweetName], startTime)

        res = []
        curr_index = starting_index
        current_interval_start = startTime
        current_interval_end = min(current_interval_start + interval_length - 1, endTime)  # inclusive
        current_interval_count = 0
        while current_interval_end <= endTime:
            # print(f'{current_interval_start} - {current_interval_end}: count:{current_interval_count} ')
            if curr_index < len(self.tweet_map[tweetName]):
                # have not run out of timestamps
                if self.tweet_map[tweetName][curr_index] <= current_interval_end:
                    # current tweet is within the current interval
                    current_interval_count += 1
                    curr_index += 1
                elif current_interval_end != endTime:
                    # push to next interval
                    current_interval_start += interval_length
                    current_interval_end = min(current_interval_end + interval_length, endTime)
                    res.append(current_interval_count)
                    current_interval_count = 0
                else:
                    res.append(current_interval_count)
                    break
            elif current_interval_end != endTime:
                # already went through all timestamps. go to the next time interval
                current_interval_start += interval_length
                current_interval_end = min(current_interval_end + interval_length, endTime)
                res.append(current_interval_count)
                current_interval_count = 0
            else:
                res.append(current_interval_count)
                break

        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

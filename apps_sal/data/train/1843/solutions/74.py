from collections import defaultdict, deque
import bisect


class TweetCounts:

    def __init__(self):
        self._deltas = {
            'minute': 60,
            'hour': 60 * 60,
            'day': 60 * 60 * 24
        }
        self._tweets = defaultdict(deque)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort_left(self._tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        tweet_times = self._tweets[tweetName]
        left = 0
        right = len(tweet_times)
        while left < right:
            mid = (left + right) // 2
            if tweet_times[mid] >= startTime:
                right = mid
            else:
                left = mid + 1
        output = [0]
        interval = self._deltas[freq]
        period_start = startTime
        while left < len(tweet_times) and tweet_times[left] <= endTime:
            if tweet_times[left] < period_start + interval:
                output[-1] += 1
                left += 1
            else:
                period_start += interval
                output.append(0)
        for _ in range((endTime - period_start) // interval):
            output.append(0)
        return output


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

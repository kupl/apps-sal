from collections import defaultdict
from enum import Enum
from math import ceil

frequency = Enum(
    value='frequency',
    names=[
        ('minute', 60),
        ('hour', 3600),
        ('day', 86400)
    ])


class TweetManager:
    def __init__(self):
        self.tweets = defaultdict(list)

    def __str__(self):
        return str(self.tweets)

    def add_tweet(self, tweet_name, time):
        self.tweets[tweet_name].append(time)
        self.tweets[tweet_name].sort()

    def _find_start_index(self, history: List[int], start_time, min_index=None, max_index=None):
        if min_index is None:
            min_index = 0
        if max_index is None:
            max_index = len(history) - 1
        if min_index > max_index:
            return None
        middle_index = int((max_index + min_index) / 2)
        if history[middle_index] == start_time:
            return middle_index
        if history[middle_index] > start_time:
            result = self._find_start_index(history, start_time, min_index, middle_index - 1)
            if result is None:
                return middle_index
            return result
        if history[middle_index] < start_time:
            return self._find_start_index(history, start_time, middle_index + 1, max_index)

    def _find_end_index(self, history: List[int], end_time, min_index=None, max_index=None):
        if min_index is None:
            min_index = 0
        if max_index is None:
            max_index = len(history) - 1
        if min_index > max_index:
            return None
        middle_index = int((max_index + min_index) / 2)
        if history[middle_index] == end_time:
            return middle_index
        if history[middle_index] > end_time:
            return self._find_end_index(history, end_time, min_index, middle_index - 1)
        if history[middle_index] < end_time:
            result = self._find_end_index(history, end_time, middle_index + 1, max_index)
            if result is None:
                return middle_index
            return result

    def _calculate_frequency(self, history: List[int], start_index, end_index, freq, end_time, start_time):

        if start_index is None or end_index is None:
            history = []
        else:
            history = history[start_index:end_index + 1]

        previous_bucket = None
        result = []
        bucket = None
        for time_seconds in history:
            bucket = 0 if (time_seconds + 1 - start_time) / frequency[freq].value <= 1 else int((time_seconds + 1 - start_time) / frequency[freq].value)

            empty_buckets = bucket - (previous_bucket if previous_bucket else 0)
            if previous_bucket is None:
                empty_buckets += 1
            if empty_buckets > 1:
                for a in range(empty_buckets):
                    result.append(0)

            if len(result) == bucket:
                result.append(1)
            else:
                result[bucket] += 1

            previous_bucket = bucket

        max_bucket = 0 if (end_time - start_time) / frequency[freq].value < 1 else int((end_time - start_time) / frequency[freq].value)

        if bucket is None:
            while max_bucket >= 0:
                result.append(0)
                max_bucket -= 1
        else:
            while max_bucket > bucket:
                result.append(0)
                max_bucket -= 1

        return result

    def get_tweet_frequency(self, tweet_name: str, start_time: int, end_time: int, freq) -> List[int]:
        start_index = self._find_start_index(self.tweets.get(tweet_name), start_time)
        end_index = self._find_end_index(self.tweets.get(tweet_name), end_time)

        result_frequency = self._calculate_frequency(self.tweets.get(tweet_name), start_index, end_index, freq, end_time, start_time)

        return result_frequency


class TweetCounts:
    def __init__(self):
        self.tweets = TweetManager()

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.add_tweet(tweetName, time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        return self.tweets.get_tweet_frequency(tweetName, startTime, endTime, freq)

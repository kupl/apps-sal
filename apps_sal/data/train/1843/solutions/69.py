from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 60*SECONDS_PER_MINUTE
SECONDS_PER_DAY = 24*SECONDS_PER_HOUR
INTERVAL_LENGTH = {
    'minute': SECONDS_PER_MINUTE,
    'hour': SECONDS_PER_HOUR,
    'day': SECONDS_PER_DAY,
}

class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        # print(f'record {tweetName} at {time}')
        self.tweets[tweetName].add(time)
        # print(f'tweets[tweetName]: {self.tweets[tweetName]}')

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        # print(f'freq={freq} tweetName={tweetName} startTime={startTime} endTime={endTime}')

        if freq not in INTERVAL_LENGTH:
            raise Exception(f'Expected freq to be one of {INTERVAL_LENGTH.keys()}, got {freq} instead')

        if tweetName not in self.tweets:
            raise Exception(f'Unknown tweet: {tweetName}')

        intervalLength = INTERVAL_LENGTH[freq]
        numIntervals = (endTime - startTime + intervalLength) // intervalLength

        counts = []
        for i in range(numIntervals):
            intervalStart = startTime + i*intervalLength
            intervalEnd = min(intervalStart + intervalLength, endTime + 1)
            matchingTimes = self.tweets[tweetName].irange(minimum=intervalStart, maximum=intervalEnd, inclusive=(True, False))
            counts.append(len(list(matchingTimes)))

        # print(f'counts: {counts}')
        return counts


from collections import defaultdict


class TweetCounts:

    def __init__(self):
        self.data = defaultdict(list)

    def recordTweet(self, tweetName, time):
        self.data[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        start = startTime
        res = []
        self.data[tweetName].sort()
        while start <= endTime:
            end = min(start + delta, endTime + 1)
            res.append(len([x for x in self.data[tweetName] if start <= x < end]))
            start += delta
        return res

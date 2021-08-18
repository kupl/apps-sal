from collections import defaultdict


class TweetCounts:
    def __init__(self):
        self.data = defaultdict(list)

    def recordTweet(self, tweetName, time):
        self.data[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        new_data = [x for x in self.data[tweetName] if startTime <= x <= endTime]
        delta_data = [(x - startTime) // delta for x in new_data]
        n = (endTime - startTime) // delta + 1
        res = [len([x for x in delta_data if x == i]) for i in range(n)]
        return res

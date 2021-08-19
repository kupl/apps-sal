from collections import defaultdict
from bisect import bisect_left, insort


class TweetCounts:

    def __init__(self):
        self.history = defaultdict(list)

    def recordTweet(self, tweet, t):
        insort(self.history[tweet], t)

    def getTweetCountsPerFrequency(self, freq, tweet, s, e):
        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 3600
        else:
            delta = 86400
        (A, cur) = (self.history[tweet], s)
        res = []
        while cur <= e:
            nxt = min(cur + delta, e + 1)
            occurence = bisect_left(A, nxt) - bisect_left(A, cur)
            res.append(occurence)
            cur += delta
        return res

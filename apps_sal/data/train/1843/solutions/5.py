class TweetCounts:

    def __init__(self):
        from bisect import bisect_left, bisect_right
        from functools import lru_cache
        self.tweets = {}
        self.cache = {}
        return

    def recordTweet(self, tweetName: str, time: int) -> None:
        (tn, seconds) = (tweetName, time)
        if tn not in self.tweets:
            self.tweets[tn] = Counter()
        self.tweets[tn] += Counter(dict([(seconds, 1)]))
        return

    def quantize(self, per_second_tweet_counter, valid_times, scale):
        t = [((timekey - self.st) // scale, per_second_tweet_counter[timekey]) for timekey in valid_times]
        (qcnts, qkeys) = ({}, [])
        for (tk, tc) in t:
            if tk not in qcnts:
                qcnts[tk] = 0
                qkeys.append(tk)
            qcnts[tk] += tc
        n = (self.et - self.st + 1) // scale
        if (self.et - self.st + 1) % scale:
            n += 1
        res = [0] * n
        for tk in qkeys:
            res[tk] = qcnts[tk]
        return res

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        (M, H, D) = (60, 60 * 60, 60 * 60 * 24)
        (self.tn, self.st, self.et) = (tweetName, startTime, endTime)
        if self.tn not in self.tweets:
            return [0]
        per_second_tweet_counter = self.tweets[self.tn]
        key = (self.tn, self.st, self.et)
        if key in self.cache:
            valid_times = self.cache
        else:
            valid_times = [timekey for timekey in per_second_tweet_counter if self.st <= timekey <= self.et]
        if freq == 'minute':
            return self.quantize(per_second_tweet_counter, valid_times, M)
        if freq == 'hour':
            return self.quantize(per_second_tweet_counter, valid_times, H)
        if freq == 'day':
            return self.quantize(per_second_tweet_counter, valid_times, D)
        return [0]

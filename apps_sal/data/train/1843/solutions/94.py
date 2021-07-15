class TweetCounts:

    def __init__(self):
        from bisect import bisect_left, bisect_right
        from functools import lru_cache
        self.tweets = {}
        return


    def recordTweet(self, tweetName: str, time: int) -> None:
        tn, seconds = tweetName, time
        if tn not in self.tweets: self.tweets[tn] = Counter()
        self.tweets[tn] += Counter(dict([(seconds, 1)]))
        return


    def quantize(self, per_second_tweet_counter, valid_times, scale):
        t = [((timekey-self.st)//scale, per_second_tweet_counter[timekey]) 
             for timekey in valid_times]
        
        qcnts, qkeys = {}, []
        for tk, tc in t:
            if tk not in qcnts:
                qcnts[tk] = 0
                qkeys.append(tk)
            qcnts[tk] += tc

        #qkeys = list(qcnts.keys())
        n = (self.et - self.st + 1) // scale
        if (self.et - self.st + 1) % scale: n += 1
        res = [0] * (n)
        for tk in qkeys: res[tk] = qcnts[tk]
        return res

    @lru_cache
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        M, H, D = 60, 60*60, 60*60*24
        tn, st, et = tweetName, startTime, endTime
        if tn not in self.tweets: return [0]
        self.st, self.et = st, et

        per_second_tweet_counter = self.tweets[tn]
        valid_times = [timekey for timekey in per_second_tweet_counter
                       if st <= timekey <= et]

        if freq == 'minute': return self.quantize(per_second_tweet_counter, valid_times, M)
        if freq == 'hour': return self.quantize(per_second_tweet_counter, valid_times, H)
        if freq == 'day': return self.quantize(per_second_tweet_counter, valid_times, D)
        
        return [0]


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)


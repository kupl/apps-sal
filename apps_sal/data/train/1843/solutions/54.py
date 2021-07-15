from collections import defaultdict
from bisect import bisect_left, bisect_right

TIME_OFFSETS = {
    \"minute\": 60,
    \"hour\": 60 * 60,
    \"day\": 24 * 60 * 60
}

class TweetCounts:

    def __init__(self):
        self._tweets = defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        tweets = self._tweets[tweetName]
        
        pos = bisect_left(tweets, time)
        self._tweets[tweetName] = tweets[:pos] + [time] + tweets[pos:]
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        tweets = self._tweets[tweetName]
        if not tweets:
            return 0
        
        offset = TIME_OFFSETS[freq]
        result = []
        
        for t in range(startTime, endTime + 1, offset):
            t2 = min(endTime, t + offset - 1)
            pos = bisect_left(tweets, t)
            end_pos = bisect_right(tweets, t2)
            result.append(end_pos - pos)
            pos = end_pos

        return result
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

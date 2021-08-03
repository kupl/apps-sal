import collections
import bisect

class TweetCounts:
    
    FREQ_TO_SECONDS = {
        \"minute\": 60,
        \"hour\": 60*60,
        \"day\": 24*60*60,
    }

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        
        self.tweets[tweetName].insert(bisect.bisect_left(self.tweets[tweetName], time), time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = self.FREQ_TO_SECONDS[freq]
        tweets = self.tweets.get(tweetName, [])
        results = []
        
        if not tweets:
            return []
        
        while startTime <= endTime:
            upper_bound = min(endTime, startTime+delta-1)
            values = [time for time in tweets if time>=startTime and time<=upper_bound]
            results.append(len(values))
            startTime += delta
            
        return results
        
        
        
        
        
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

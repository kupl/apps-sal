from collections import defaultdict
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        times = self.tweets[tweetName]
        
        if freq == \"minute\":
            seconds = 60
        elif freq == \"hour\":
            seconds = 60 * 60
        elif freq == \"day\":
            seconds = 60 * 60 * 24
        
        output_len = ((endTime - startTime)/seconds) + 1
        output = [0] * int(output_len)
        
        for time in times:
            if time >= startTime and time <= endTime:
                index = int((time - startTime)/seconds)
                output[index] += 1
        
        return output
    
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)


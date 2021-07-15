# similiar : design-log-storage-system-635
class TweetCounts:

    def __init__(self):
        self.__records = collections.defaultdict(list)
        self.__lookup = {\"minute\": 60, \"hour\": 3600, \"day\": 86400}
        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.__records[tweetName].append(time)



    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = self.__lookup[freq]
        result = [0] * ((endTime - startTime) // delta + 1)
        for t in self.__records[tweetName]:
            if startTime <= t <= endTime:
                result[(t - startTime) // delta] += 1
        return result
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)


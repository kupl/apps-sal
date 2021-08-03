from sortedcontainers import SortedList
class TweetCounts:

    def __init__(self):
        self.timeStamps = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.timeStamps:
            self.timeStamps[tweetName] = SortedList({})
        self.timeStamps[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = None
        if freq == \"minute\":
            delta = 60
        elif freq == \"hour\":
            delta = 3600
        else:
            delta = 86400
        answer = []
        ##need to essentially figure out the first tweet in self.timeStamps[tweetName] that comes at least at startTime and then go on by the delta until we see that we exceed endTime. We will have to stop along the way if our endTime is greater than current time plus delta and then append to answer and create new List.
        if tweetName in self.timeStamps:
            startIndex = self.timeStamps[tweetName].bisect_left(startTime)
            timeStampLength = len(self.timeStamps[tweetName])
            currentIndex = startIndex
            lowerBound = startTime
            upperBound = min(lowerBound+delta-1,endTime)
            while True:##if we see that the currentIndex is already too large then we will have that the count = 0
                count = 0
                currentTime = self.timeStamps[tweetName][currentIndex] if currentIndex < timeStampLength else float('inf')##this will ensure that we still put in 0s for count if our timestamp is way to far ahead already
                while currentTime >= lowerBound and upperBound >= currentTime:
                    count += 1
                    currentIndex += 1
                    if currentIndex >= timeStampLength:
                        break
                    else:
                        currentTime = self.timeStamps[tweetName][currentIndex]
                answer.append(count)
                lowerBound += delta
                if lowerBound > endTime:
                    break
                else:
                    upperBound = min(lowerBound+delta-1,endTime)
        return answer


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

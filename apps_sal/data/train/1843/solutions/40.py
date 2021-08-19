from collections import defaultdict
from bisect import insort, bisect_left


class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.d = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        # insort(self.tweets[tweetName], time)
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        record = self.tweets[tweetName]
        delta = self.d[freq]
        # Solution 2: loop through the whole record O(n)
        res = [0] * ((endTime - startTime) // delta + 1)  # total interval
        for time in record:  # loop through time in record
            if time < startTime or time > endTime:
                continue
            res[(time - startTime) // delta] += 1
        return res
        # Solution 1: Binary search O(logn)
        # res = []
        # i = startTime
        # while i <= endTime:
        #     j = min(i + delta, endTime + 1)
        #     res.append(bisect_left(record, j) - bisect_left(record, i))
        #     i += delta
        # return res

        # not efficient solution
        # low = bisect_left(record, startTime)
        # res = [0]
        # start, idx, j = startTime, low, 1
        # print (record[idx:], startTime, endTime, delta)
        # while idx < len(record) and record[idx] <= endTime:
        #     if record[idx] < start + delta*j:
        #         res[j-1] += 1
        #     else:
        #         j += 1
        #         res.append(1)
        #         start += delta
        #     idx += 1
        # print (res)
        # return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

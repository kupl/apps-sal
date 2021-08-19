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

        # delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        # start = startTime
        # res = []
        # while start <= endTime:
        #     end = min(start + delta, endTime + 1)
        #     res.append(len([x for x in self.data[tweetName] if start <= x < end]))
        #     start += delta
        # return res

        # delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        # start = startTime
        # res = []
        # self.data[tweetName].sort()
        # while start <= endTime:
        #     end = min(start + delta, endTime + 1)
        #     res.append(len([x for x in self.data[tweetName] if start <= x < end]))
        #     # res.append(bisect_left(self.data[tweetName], end) - bisect_left(self.data[tweetName], start))
        #     start += delta
        # return res

# class TweetCounts:
#     def __init__(self):
#         self.data = defaultdict(list)

#     def recordTweet(self, tweetName, time):
#         bisect.insort(self.data[tweetName], time)

#     def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
#         delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
#         i = startTime
#         res = []
#         while i <= endTime:
#             j = min(i + delta, endTime + 1)
#             res.append(bisect_left(self.data[tweetName], j) - bisect_left(self.data[tweetName], i))
#             i += delta
#         return res


# from collections import defaultdict
# class TweetCounts:

#     def __init__(self):
#         self.a = defaultdict(list)


#     def recordTweet(self, tweetName: str, time: int) -> None:
#         bisect.insort(self.a[tweetName], time)


#     def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
#         delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
#         i = startTime
#         res = []
#         while i <= endTime:
#             j = min(i + delta, endTime + 1)
#             res.append(bisect_left(self.a[tweetName], j) - bisect_left(self.a[tweetName], i))
#             i += delta
#         return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.mapping = {'minute': 60, 'hour': 3600, 'day': 86400}

    def binary_search(self, left, right, key, array, type):
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] >= key:
                right = mid - 1
            else:
                left = mid + 1
        return left if type == 'S' else right

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        self.tweets[tweetName].sort()
        tweetcounts = self.tweets[tweetName]
        intervals = []
        while startTime < endTime + 1:
            startindex = self.binary_search(0, len(tweetcounts) - 1, startTime, tweetcounts, 'S')
            findval = min(startTime + self.mapping[freq], endTime + 1)
            endindex = self.binary_search(0, len(tweetcounts) - 1, findval, tweetcounts, 'E')
            intervals.append(endindex - startindex + 1)
            startTime += self.mapping[freq]
        return intervals

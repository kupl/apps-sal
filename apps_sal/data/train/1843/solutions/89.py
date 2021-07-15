import collections


class TweetCounts(object):

\tdef __init__(self):
\t\tself.tweets = collections.defaultdict(list)

\tdef recordTweet(self, tweetName, time):
\t\tself.tweets[tweetName].insert(self.binary_search(tweetName, time),  time)


\tdef getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
\t\tdelta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
\t\ti = startTime
\t\tres = []
\t\twhile i <= endTime:
\t\t\tj = min(i + delta, endTime + 1)
\t\t\tres.append(self.binary_search(tweetName, j) - self.binary_search(tweetName, i))
\t\t\ti += delta

\t\treturn res


\tdef binary_search(self, tweetName, time):
\t\tcur_list = self.tweets[tweetName]
\t\tl = 0
\t\tr = len(cur_list) 
\t\twhile l < r:
\t\t\tmid = (l+r) // 2
\t\t\tif cur_list[mid] < time:
\t\t\t\tl = mid + 1
\t\t\telse:
\t\t\t\tr = mid

\t\treturn l

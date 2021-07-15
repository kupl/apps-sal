## Basic Ideas: Two hashmap + PriorityQueue
 ##     tweet_dict. id -> tweet_list
 ##     follow_dict: id -> id set
 ##
 ## Notice: people may follow themselves
 ##
 ## Assumption: people tweet with post id always grows
 ##
 ## Complexity: getNewsFeed
 ##       Time O(n*log(n)) Space O(n). n = total tweets involved
 import collections, copy
 class Twitter:
 
     def __init__(self):
         """
         Initialize your data structure here.
         """
         self.id = 0
         self.tweet_dict = collections.defaultdict(lambda: [])
         self.follow_dict = collections.defaultdict(lambda: set([]))
 
     def postTweet(self, userId, tweetId):
         """
         Compose a new tweet.
         :type userId: int
         :type tweetId: int
         :rtype: void
         """
         self.tweet_dict[userId].append((self.id, tweetId))
         self.id += 1
 
     def getNewsFeed(self, userId):
         """
         Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
         :type userId: int
         :rtype: List[int]
         """
         q = []
         # min heap
         heapq.heapify(q)
         for (id, tweetId) in self.tweet_dict[userId]:
             heapq.heappush(q, (id, tweetId))
             if len(q) > 10: heapq.heappop(q)
         for followee in self.follow_dict[userId]:
             for (id, tweetId) in self.tweet_dict[followee]:
                 heapq.heappush(q, (id, tweetId))
                 if len(q) > 10: heapq.heappop(q)
         res = []
         while len(q) != 0:
             (id, tweetId) = heapq.heappop(q)
             res.insert(0, tweetId)
         return res
 
     def follow(self, followerId, followeeId):
         """
         Follower follows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         if followerId == followeeId: return
         if followeeId not in self.follow_dict[followerId]:
             self.follow_dict[followerId].add(followeeId)
 
     def unfollow(self, followerId, followeeId):
         """
         Follower unfollows a followee. If the operation is invalid, it should be a no-op.
         :type followerId: int
         :type followeeId: int
         :rtype: void
         """
         if followerId == followeeId: return
         if followeeId in self.follow_dict[followerId]:
             self.follow_dict[followerId].remove(followeeId)
 
 
 # Your Twitter object will be instantiated and called as such:
 # obj = Twitter()
 # obj.postTweet(userId,tweetId)
 # param_2 = obj.getNewsFeed(userId)
 # obj.follow(followerId,followeeId)
 # obj.unfollow(followerId,followeeId)

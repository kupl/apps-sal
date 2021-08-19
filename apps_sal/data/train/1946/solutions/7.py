class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # e.g. [{"user1":"tweet1"}, {"user2":"tweet2"},...] - fast tweets access
        self.tweets = []

        # e.g. {"user1":[0,2,4,5], "user2":[1,3]} - fast user-tweets access
        self.userTweets = {}

        # e.g. {"user1":[0,1,2,3,4,5]}
        self.feeds = {}

        # e.g. {user2:[1]}
        self.followers = {}
        self.followees = {}
        # eg. {(user1,user2):True}
        self.relations = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        # create tweet
        self.tweets.append({"userId": userId, "tweetId": tweetId})
        lastIndex = len(self.tweets) - 1

        # create user tweet list
        if userId not in self.userTweets:
            self.userTweets[userId] = []
        self.userTweets[userId].append(lastIndex)

        # update feeds
        followers = self.followers.get(userId, [])
        for followerId in [userId] + followers:
            # add tweet, reverse sort, cut recent 10
            self.feeds[followerId] = ([tweetId] + self.feeds.get(followerId, []))[:10]

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        return self.feeds.get(userId, [])

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # no-op case
        if (followerId, followeeId) in self.relations or followerId == followeeId:
            return
        else:
            self.relations[(followerId, followeeId)] = True

        #  add follower, create new list if not exist
        if followeeId not in self.followers:
            self.followers[followeeId] = []
        self.followers[followeeId].append(followerId)

        # add followee
        if followerId not in self.followees:
            self.followees[followerId] = []
        self.followees[followerId].append(followeeId)

        # update user's feed
        self.updateFeed(followerId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        # no-op case
        if (followerId, followeeId) not in self.relations:
            return
        else:
            del self.relations[(followerId, followeeId)]

        # remove relation
        self.followers[followeeId].remove(followerId)
        self.followees[followerId].remove(followeeId)

        # skip update if followee didn't tweet
        if not self.userTweets.get(followeeId, []):
            return

        # full rebuild feed
        self.updateFeed(followerId)

    def updateFeed(self, userId):
        # full rebuild feed
        followers = self.followees.get(userId, [])
        indexes = []
        for followeeId in [userId] + followers:
            if self.userTweets.get(followeeId, []):
                indexes += self.userTweets.get(followeeId, [])
                indexes = sorted(indexes, reverse=True)[0:10]

        # set new feed
        self.feeds[userId] = [self.tweets[idx]['tweetId'] for idx in indexes]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.userTweets = {}
        self.feeds = {}
        self.followers = {}
        self.followees = {}
        self.relations = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets.append({'userId': userId, 'tweetId': tweetId})
        lastIndex = len(self.tweets) - 1
        if userId not in self.userTweets:
            self.userTweets[userId] = []
        self.userTweets[userId].append(lastIndex)
        followers = self.followers.get(userId, [])
        for followerId in [userId] + followers:
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
        if (followerId, followeeId) in self.relations or followerId == followeeId:
            return
        else:
            self.relations[followerId, followeeId] = True
        if followeeId not in self.followers:
            self.followers[followeeId] = []
        self.followers[followeeId].append(followerId)
        if followerId not in self.followees:
            self.followees[followerId] = []
        self.followees[followerId].append(followeeId)
        self.updateFeed(followerId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if (followerId, followeeId) not in self.relations:
            return
        else:
            del self.relations[followerId, followeeId]
        self.followers[followeeId].remove(followerId)
        self.followees[followerId].remove(followeeId)
        if not self.userTweets.get(followeeId, []):
            return
        self.updateFeed(followerId)

    def updateFeed(self, userId):
        followers = self.followees.get(userId, [])
        indexes = []
        for followeeId in [userId] + followers:
            if self.userTweets.get(followeeId, []):
                indexes += self.userTweets.get(followeeId, [])
                indexes = sorted(indexes, reverse=True)[0:10]
        self.feeds[userId] = [self.tweets[idx]['tweetId'] for idx in indexes]

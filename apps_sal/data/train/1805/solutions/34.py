class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        friends = getFriends(friends, id, 1, level, set([id]))
        videoCounts = collections.Counter([val for i in friends for val in watchedVideos[i]])
        sortedCounts = sorted(list(videoCounts.items()), key=lambda video: (video[1], video[0]))
        return [count[0] for count in sortedCounts]


def getFriends(friends: List[List[int]], index: int, level: int, targetLevel: int, knownFriends):
    currentFriends = set(friends[index]) - knownFriends
    if level == targetLevel:
        return currentFriends
    else:
        newKnownFriends = knownFriends | currentFriends
        return set([val for i in currentFriends for val in getFriends(friends, i, level + 1, targetLevel, newKnownFriends)])

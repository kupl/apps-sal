from collections import Counter


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        friendsSeen = {id}
        k = 0

        connections = {id}
        for k in range(0, level):
            nextDegree = [friends[i] for i in connections]
            connections = set([friend for friends in nextDegree for friend in friends if friend not in friendsSeen])
            friendsSeen = friendsSeen.union(connections)

        videosWatched = [video for friend in connections for video in watchedVideos[friend]]
        videoCounter = dict(Counter(videosWatched))
        result = sorted(videoCounter.keys(), key=lambda x: videoCounter[x])
        freqUnique = [videoCounter[video] for video in result]
        freqMovieDict = dict()
        for i in range(0, len(freqUnique)):
            if freqUnique[i] not in freqMovieDict:
                freqMovieDict[freqUnique[i]] = [result[i]]
            else:
                freqMovieDict[freqUnique[i]] += [result[i]]
        for key in freqMovieDict:
            freqMovieDict[key] = sorted(freqMovieDict[key])
        ans = []
        for key in sorted(freqMovieDict.keys()):
            ans += freqMovieDict[key]
        return ans

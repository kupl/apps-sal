class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        k_friends = self.findFriends(friends, [id], {id}, level)
        watched = {}
        for id in k_friends:
            for vid in watchedVideos[id]:
                if vid in watched:
                    watched[vid] += 1
                else:
                    watched[vid] = 1

        out = []
        for key in watched:
            out.append((watched[key], key))
        out.sort()

        return list([x[1] for x in out])

    def findFriends(self, friends, ids, seen, level):
        if level == 0 or len(ids) == 0:
            return ids

        new = []
        for id in ids:
            for friend in friends[id]:
                if friend not in seen:
                    seen.add(friend)
                    new.append(friend)

        return self.findFriends(friends, new, seen, level - 1)

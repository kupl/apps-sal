class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        (w, f) = ({}, {})
        for i in range(len(friends)):
            w[i] = watchedVideos[i]
            f[i] = friends[i]
        cand = []
        frontier = [(id, 0)]
        seen = {id}
        while frontier:
            (cur, d) = frontier.pop()
            if d == level:
                cand.append(cur)
                continue
            for friend in f[cur]:
                if friend not in seen:
                    seen.add(friend)
                    frontier.append((friend, d + 1))
        count = collections.Counter()
        for c in cand:
            for m in w[c]:
                count[m] += 1
        ans = [(v, k) for (k, v) in count.items()]
        ans.sort()
        ans = [x[1] for x in ans]
        return ans

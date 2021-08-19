class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        dist = [9999] * n
        queue = [(id, 0)]
        while queue:
            (idx, depth) = queue.pop(0)
            if depth < dist[idx]:
                dist[idx] = depth
                for c in friends[idx]:
                    queue.append((c, depth + 1))
        print(dist)
        freq = defaultdict(int)
        for (i, l) in enumerate(dist):
            if l == level:
                for vid in watchedVideos[i]:
                    freq[vid] += 1
        pairs = sorted([(v, k) for (k, v) in list(freq.items())])
        print(pairs)
        return [x[-1] for x in pairs]

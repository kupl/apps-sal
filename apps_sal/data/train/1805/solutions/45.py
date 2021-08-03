import collections


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # First: walk friends and summarize k-level info
        krem = set(range(len(friends)))
        krem.remove(id)

        curlevel = 0
        klevel = set([id])
        while True:
            # print(\"level: {} members: {}\".format(curlevel, klevel))
            if curlevel == level:
                break

            newlevel = set()

            # We will only walk each 'pid' exactly once
            for pid in klevel:
                # Therefore we will only walk friends-of-pid exactly once
                for fid in friends[pid]:
                    # Not shortest path to 'fid'
                    if not fid in krem:
                        continue

                    krem.remove(fid)
                    newlevel.add(fid)

            klevel = newlevel
            curlevel += 1

        krem = None

        # klevel now is the set of ids reachable at shortest-path 'k' from 'id'
        # So we just need to identify the videos.
        vids = collections.defaultdict(int)
        for pid in klevel:
            for vid in watchedVideos[pid]:
                vids[vid] += 1

        return [x[0] for x in sorted(vids.items(), key=lambda x: (x[1], x[0]))]

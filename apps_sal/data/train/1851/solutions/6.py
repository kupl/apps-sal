class Solution:
    import json

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        IMPOSSIBLE = float('inf')
        sorted_clips = sorted(clips, key=lambda x: x[0], reverse=False)
        opt = {}
        for index, clip in enumerate(sorted_clips):
            for t in range(0, T + 1):
                start, end = tuple(clip)
                if t == 0:
                    opt[index, t] = 0
                elif index == 0:
                    opt[index, t] = 1 if start == 0 and t <= end else IMPOSSIBLE
                else:
                    opt[index, t] = min(opt[index - 1, t], opt[index - 1, min(start, t)] + 1 if t <= end else IMPOSSIBLE)
        print(opt)
        return opt[len(clips) - 1, T] if opt[len(clips) - 1, T] != float('inf') else -1

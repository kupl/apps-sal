class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # First find clips that start from 0
        # Then use the clip that reaches the farthest
        # Continually find clips that continue, and pick ones that reach the farthest

        last_end = 0
        clip_count = 0
        while last_end < T:
            # If no more clips
            if clip_count >= len(clips):
                return -1
            # Find valid clip that reaches the farthest
            max_end = -1
            for clip in clips:
                if clip[0] <= last_end:
                    if clip[1] > max_end:
                        max_end = clip[1]

            if max_end >= 0:
                last_end = max_end
                clip_count += 1
            else:
                return -1

        return clip_count

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        table = [101] * 101
        table[0] = 0

        changed = True
        while changed:
            changed = False
            for i, j in clips:
                for k in range(i, j + 1):
                    if table[i] + 1 < table[k]:
                        table[k] = table[i] + 1
                        changed = True

        if table[T] < 101:
            return table[T]
        else:
            return -1

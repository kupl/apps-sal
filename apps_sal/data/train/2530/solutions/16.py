class Solution:

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        offset_from_60 = {}
        for duration in time:
            offset = duration % 60
            if offset in offset_from_60:
                offset_from_60[offset].append(duration)
            else:
                offset_from_60[offset] = [duration]
        key_pairs = []
        sorted_keys = sorted(list(offset_from_60.keys()))
        for key in [k for k in sorted_keys if k <= 30]:
            if 60 - key in sorted_keys:
                key_pairs.append((key, 60 - key))
            if key == 0:
                key_pairs.append((0, 0))
        count = 0
        for (k1, k2) in key_pairs:
            len_k1 = len(offset_from_60[k1])
            if k1 == 0 or k1 == 30:
                try:
                    count += math.factorial(len_k1) / (2 * math.factorial(len_k1 - 2))
                except:
                    pass
            else:
                count += len_k1 * len(offset_from_60[k2])
        return int(count)

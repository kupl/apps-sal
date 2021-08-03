class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        partial_stamps, L, N = [stamp], len(stamp), len(target)
        for covered_length in range(1, L):
            for leading in range(covered_length + 1):
                prefix, postfix = '?' * leading, '?' * (covered_length - leading)
                partial_stamps.append(prefix + stamp[leading:leading + L - covered_length] + postfix)

        reversed_positions, dest = [], '?' * N
        while target != dest:
            prev = target
            for idx in range(N - L + 1):
                p = target[idx:idx + L]
                for s in partial_stamps:
                    if p == s:
                        reversed_positions.append(idx)
                        target = target[:idx] + '?' * L + target[idx + L:]
                        break
            if prev == target:
                return []
        return reversed_positions[::-1]

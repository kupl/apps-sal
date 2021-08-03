class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if set(stamp) < set(target) or len(stamp) > len(target):
            return []

        path = []
        while target != '*' * len(target):
            prev_target = target
            for i in range(len(target) - len(stamp) + 1):
                if target[i:i + len(stamp)] == '*' * len(stamp):
                    continue
                if not all(target[i + j] in (stamp[j], '*') for j in range(len(stamp))):
                    continue

                target = target[:i] + '*' * len(stamp) + target[i + len(stamp):]
                path.append(i)

            if prev_target == target:
                return []

        return path[::-1]

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        ret = []
        stamp = list(stamp)
        target = list(target)
        cnt = 0
        candidates = [i for i in range(len(target) - len(stamp) + 1)]
        while cnt < len(target) and len(candidates) > 0:
            nxt = []
            for i in candidates:
                l = min(len(stamp), len(target) - i)
                if (all(target[i + j] in ['*', stamp[j]] for j in range(l))
                        and any(target[i + j] != '*' for j in range(l))):
                    nxt += [max(0, i - j) for j in range(l)]
                    for j in range(i, i + l):
                        if target[j] != '*':
                            cnt += 1
                        target[j] = '*'
                    ret.append(i)
            candidates = nxt

        return ret[::-1] if cnt == len(target) else []

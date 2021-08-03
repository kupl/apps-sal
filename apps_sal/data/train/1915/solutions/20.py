class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        l = len(stamp)

        @lru_cache(None)
        def dfs(i, o):
            if i == len(target):
                return []

            if not o:
                if i + l > len(target):
                    return None
                for k in range(l):
                    if i + k >= len(target) or stamp[k] != target[i + k]:
                        break
                    if dfs(i + k + 1, False) is not None:
                        return [i] + dfs(i + k + 1, False)
                else:
                    if dfs(i + k + 1, True) is not None:
                        return dfs(i + k + 1, True) + [i]
            else:
                for j in range(l):
                    if l - j + i > len(target):
                        continue
                    for k in range(j, l):
                        if i + k - j >= len(target) or stamp[k] != target[i + k - j]:
                            break
                        if dfs(i + k - j + 1, False) is not None:
                            return [i - j] + dfs(i + k - j + 1, False)
                    else:
                        if dfs(i + k - j + 1, True) is not None:
                            return dfs(i + k - j + 1, True) + [i - j]
            return None

        return dfs(0, False)

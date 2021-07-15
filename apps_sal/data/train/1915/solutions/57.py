class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if set(stamp) < set(target) or len(stamp) > len(target):
            return []
        
        patterns = set()
        for l in range(1, len(stamp) + 1):
            for i in range(len(stamp) - l + 1):
                patterns.add('*' * i + stamp[i:i + l] + '*' * (len(stamp) - i - l))
            
        goal = '*' * len(target)
        def dfs(cur, path, moves):
            if cur == goal:
                return path
            
            if not moves:
                return []
            
            old_moves = moves
            for pattern in patterns:
                i = cur.find(pattern)
                if i >= 0:
                    cur = cur[:i] + '*' * len(stamp) + cur[i + len(stamp):]
                    path.append(i)
                    moves -= 1
            
            if old_moves == moves:
                return []
            
            return dfs(cur, path, moves)
        
        return dfs(target, [], 10 * len(target))[::-1]


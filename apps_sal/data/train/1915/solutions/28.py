class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        N, M, match = len(target), len(stamp), True
        
        positions = []
        while match:
            match, idx = False, 0
            while idx <= N-M:
                match_cnt = 0
                for i in range(M):
                    if target[idx+i] == '?':
                        continue
                    if target[idx+i] != stamp[i]:
                        break
                    match_cnt += 1
                else:
                    if match_cnt:
                        positions.append(idx)
                        target = target[:idx] + '?'*M + target[idx+M:]
                        match, idx = True, idx+M-1
                idx += 1
        return positions[::-1] if target == '?'*N else []


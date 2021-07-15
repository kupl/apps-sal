class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        N , M = len(target), len(stamp)
        def cor(s):
            result = False
            for c1, c2 in zip(s,stamp):
                if c1 == '?':
                    continue
                elif c1 != c2:
                    return False
                else:
                    result = True
            return result
        base, times, max_times, indexes = '?' * N , 0 , 10* N, []                
        while times < max_times:
            start = times
            for i in range(N - M + 1):                
                if cor(target[i:i + M  ]):
                    times += 1
                    indexes.append(i)
                    target = target[:i] + '?' *  M + target[i+M:]                
            if target == base:
                return indexes[::-1]
                
            if times == start:
                break
        print(\"here\")
        return  []
            
                
                
            
            
            

from collections import Counter, defaultdict
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        memo = defaultdict(list)
        rest = 0
        for e, c in counter.most_common():
            memo[c].append(e)
            rest += c
        ret = []
        while rest:
            rest -= 1
            for c in sorted(memo.keys(), reverse=True):
                for idx, e in enumerate(memo[c]):
                    if ret and ret[-1] == e:
                        continue                
                    ret.append(e)
                    del memo[c][idx]
                    if not memo[c]:
                        del memo[c]
                    memo[c-1].append(e)
                    break
                if rest == len(barcodes) - len(ret):
                    break
                    
                    
        return ret

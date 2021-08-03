from collections import defaultdict


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ch2cnt = defaultdict(int)
        for b in B:
            tmp_cnt = defaultdict(int)
            for ch in b:
                tmp_cnt[ch] += 1
            for k, v in tmp_cnt.items():
                ch2cnt[k] = max(ch2cnt[k], v)
        res = []
        for a in A:
            tmp_dict = dict(ch2cnt)
            for ch in a:
                if ch in tmp_dict:
                    tmp_dict[ch] -= 1
                    if tmp_dict[ch] == 0:
                        tmp_dict.pop(ch)
            if len(tmp_dict) == 0:
                res.append(a)
        return res

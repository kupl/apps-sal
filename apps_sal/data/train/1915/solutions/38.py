class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        res = []
        all_len = 0
        cur_len = 1
        while cur_len:
            cur_len = 0
            for i in range(len(stamp)):
                for j in range(len(stamp) - i):
                    cur_stamp = '*' * i + stamp[i:len(stamp) - j] + '*' * j
                    idx = target.find(cur_stamp)
                    while idx != -1:
                        target = target[:idx] + '*' * len(cur_stamp) + target[idx + len(cur_stamp):]
                        res.append(idx)
                        cur_len += len(stamp) - i - j
                        idx = target.find(cur_stamp)
            all_len += cur_len
        return res[::-1] if all_len == len(target) else []

class Solution:
    def movesToStamp(self, stamp, target):
        ns = len(stamp)
        stamp_patterns = []
        # we need to collect all possible stamp patters, like
        # 'abcde'
        # 'abcd*'
        # '*bcde'
        # 'abc**'
        # '**cde'
        # 'ab***'
        # '*bc**'
        # '**cd*'
        # '***de'
        # ‘****e’ and etc
        for window_size in range(1, ns + 1):
            for i in range(ns - window_size + 1):
                curr = '*' * i + stamp[i:i + window_size] + '*' * (ns - window_size - i)
                stamp_patterns.append(curr)
        stamp_patterns.append('*' * ns)

        res = []
        nt = len(target)
        # '*****' is our final target
        while target != '*' * nt:
            old_target = target
            # greedy, keep replace current target string with possible patter
            for pattern in stamp_patterns:
                inx = target.find(pattern)
                if inx != -1:
                    target = target[:inx] + '*' * ns + target[inx + ns:]
                    res.append(inx)
            if old_target == target:
                return []

        return res[::-1]

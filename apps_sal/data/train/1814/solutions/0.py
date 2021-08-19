class Solution:

    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        fn_stk = []
        excl_time = [0] * n
        prev = 0
        if n < 1 or not logs:
            return fn_stk
        (fn, action, ts) = logs[0].split(':')
        fn_stk.append(int(fn))
        for log in logs[1:]:
            (fn, action, ts) = log.split(':')
            (fn, ts) = (int(fn), int(ts))
            if action == 'start':
                if fn_stk:
                    excl_time[fn_stk[len(fn_stk) - 1]] += ts - prev
                prev = ts
                fn_stk.append(fn)
            else:
                fid = fn_stk.pop()
                excl_time[fid] += ts - prev + 1
                prev = ts + 1
        return excl_time

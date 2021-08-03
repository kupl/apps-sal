class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0 for _ in range(n)]
        stack = []
        for log in logs:
            func, op, time = log.split(":")
            func = int(func)
            time = int(time)
            if op == "start":
                if stack:
                    func_last, time_last = stack[-1]
                    result[func_last] += time - time_last
                stack.append([func, time])
            else:
                func_last, time_last = stack.pop()
                result[func_last] += time - time_last + 1
                if stack:
                    stack[-1][1] = time + 1
        return result

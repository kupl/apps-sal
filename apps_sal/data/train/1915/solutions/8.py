class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # This is Greedy sol from https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS
        # reversely change target to **********
        # the method is once find a substring in target that equals stamp, change them to *
        # when seeing a * just continue
        # continue doing this until no matching can be found

        def check(i):
            found = False
            for j in range(len(s)):
                if t[i + j] == '*':
                    continue
                if t[i + j] != s[j]:  # substring t[i:i+m] != s
                    return False
                found = True
            if found:
                t[i:i + len(s)] = ['*'] * len(s)
                res.append(i)
            return found

        n, m, t, s, res = len(target), len(stamp), list(target), list(stamp), []
        while True:
            found = False
            for i in range(n - m + 1):
                found = found or check(i)
            if not found:
                break
        return res[::-1] if t == ['*'] * n else []

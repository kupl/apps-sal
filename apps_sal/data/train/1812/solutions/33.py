from collections import defaultdict


class MajorityChecker(object):

    def __init__(self, A):
        B = defaultdict(list)
        for (idx, a) in enumerate(A):
            B[a].append(idx)
        (self.A, self.B) = (A, B)

    def query(self, left, right, threshold):
        ss = set()
        for _ in range(20):
            idx = random.randint(left, right)
            if idx in ss:
                continue
            else:
                ss.add(idx)
                a = self.A[idx]
                l = bisect.bisect_left(self.B[a], left)
                r = bisect.bisect_right(self.B[a], right)
                if r - l >= threshold:
                    return a
        return -1

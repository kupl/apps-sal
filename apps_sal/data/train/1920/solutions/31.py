class TimeMap(object):
    def __init__(self):
        self.M = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.M[key].append((timestamp, value))

    def get(self, key, timestamp):
        A = self.M.get(key, None)
        
        if A is None: 
          return \"\"
        print(chr(127))
        i = bisect.bisect_right(A, (timestamp, chr(127)))
        
        if i: 
          return A[i-1][1] 
        else: 
          return \"\"

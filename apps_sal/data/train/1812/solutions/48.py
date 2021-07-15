class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.data = defaultdict(list)
        for i,num in enumerate(arr):
            self.data[num] += [i]

    def query(self, left: int, right: int, threshold: int) -> int:
        counter = defaultdict(int)
        for _ in range(32):
            index = random.randint(left, right)
            counter[self.arr[index]] += 1
        max_cnts = sorted([(value,key) for key,value in list(counter.items())], reverse=True)[:2]
        
        for value,key in max_cnts:
            i = bisect.bisect_left(self.data[key],  left)
            j = bisect.bisect_right(self.data[key], right)
            if j - i >= threshold:
                return key
        return -1
        
# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)


class MajorityChecker:
    def __init__(self, nums):
        atoi = defaultdict(list)
        for i, num in enumerate(nums):
            atoi[num].append(i)
        self.nums = nums
        self.atoi = atoi

    def query(self, left, right, threshold):
        for _ in range(20):
            rand = self.nums[random.randint(left, right)]
            left_element = bisect.bisect_left(self.atoi[rand], left)
            right_element = bisect.bisect(self.atoi[rand], right) 
            if right_element - left_element >= threshold:
                return rand
        return -1

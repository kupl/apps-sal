nums = set()
for i in range(35):
    for j in range(25):
        for k in range(15):
            nums.add(2**i * 3**j * 5**k)
nums = [None] + sorted(nums)

def hamming(n):
    return nums[n]

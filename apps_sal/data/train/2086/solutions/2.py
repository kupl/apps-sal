(n, q) = list(map(int, input().split()))
nums = list(map(int, input().split()))
'\nalgo:\nstore the combos until the maximum element reaches the front of the deque\nthen the order of the rest of the deque only changes by 2nd element going to end\nso let cutoff = number of operation which causes the max element to reach front\nif mj <= cutoff then output mjth combo stored\nif mj > cutoff  then output = (max, (mj-cutoff-1)%(len-1)+1)\n'
m = max(nums)
ab = []
while nums[0] < m:
    ab.append([nums[0], nums[1]])
    nums.append(nums.pop(1)) if nums[0] > nums[1] else nums.append(nums.pop(0))
for i in range(q):
    mj = int(input())
    (a, b) = list(map(str, ab[mj - 1] if mj <= len(ab) else (m, nums[(mj - len(ab) - 1) % (len(nums) - 1) + 1])))
    print(a + ' ' + b)

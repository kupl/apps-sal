target = 2000


def finds(nums, target):
    tmp_map = {}
    for index, num in enumerate(nums):
        if target - num in tmp_map:
            return [index, tmp_map[target - num]]
        tmp_map[num] = index


for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    if (finds(nums, target)) == None:
        print("Rejected")
    else:
        print("Accepted")

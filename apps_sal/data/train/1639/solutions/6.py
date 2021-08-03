from itertools import cycle, permutations


def gta(limit, *args):
    nums = []
    numbers = [str(n) for n in args]
    for i in cycle(range(len(numbers))):
        if numbers[i]:
            if int(numbers[i][0]) not in nums:
                nums.append(int(numbers[i][0]))
                if len(nums) == limit:
                    break
            numbers[i] = numbers[i][1:]
        elif "".join(numbers) == "":
            break
    ans = 0
    for n in range(1, len(nums) + 1):
        for arr in permutations(nums, n):
            ans += sum(arr)
    return ans

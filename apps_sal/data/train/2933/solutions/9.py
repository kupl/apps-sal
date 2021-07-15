def solve(nums,div):
    if nums == []:
        return []
    output = []
    for num in nums:
        output.append((num % div) + num)
    return output


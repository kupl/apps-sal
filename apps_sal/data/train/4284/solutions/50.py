def array_leaders(numbers):
    ans = []
    for i in range(len(numbers)-1):
        if numbers[i]>sum(numbers[i+1:]):
            ans.append(numbers[i])
    if numbers[-1]>0:
            ans.append(numbers[-1])
    return ans

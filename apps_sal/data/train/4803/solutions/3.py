def two_sum(numbers, target):
    for i in range(0, len(numbers)):
        for x in range(0, len(numbers)):
            if numbers[i] + numbers[x] == target and i != x:
                index1 = i
                index2 = x
                break
    return sorted([index1, index2])

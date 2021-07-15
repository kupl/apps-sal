def highest_rank(arr):
    print(arr)
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            mx = [0,0]
    maxes = []
    for num in freq:
        if freq[num] > mx[1]:
            mx[0] = num
            mx[1] = freq[num]
            maxes = [num]
        elif freq[num] == mx[1]:
            maxes.append(num)

    return max(maxes)


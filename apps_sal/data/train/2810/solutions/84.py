def solve(arr):
    res = []
    for word in arr:
        sum = 0
        for index, letter in enumerate(word.lower()):
            if (index + 1) == (ord(letter) - 96):
                sum += 1
        res.append(sum)

    return res

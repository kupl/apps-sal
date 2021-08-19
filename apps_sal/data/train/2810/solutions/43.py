def solve(arr):
    res = []
    count = 0
    for word in arr:
        for i in range(len(word)):
            if i == ord(word.lower()[i]) - 97:
                count += 1
        res.append(count)
        count = 0
    return res

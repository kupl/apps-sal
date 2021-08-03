def solve(arr):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for word in arr:
        count = 0
        for i in range(len(word)):
            try:
                if word[i].lower() == alpha[i]:
                    count += 1
            except IndexError:
                count = count
        res.append(count)
    return res

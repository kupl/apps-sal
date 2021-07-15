def solve(arr):
    result = []
    for word in arr:
        cnt = 0
        for idx in range(len(word)):
            if ord(word[idx].lower()) - ord('a') == idx:
                cnt += 1
        result.append(cnt)
    return result

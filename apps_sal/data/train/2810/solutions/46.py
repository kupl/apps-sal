def solve(arr):
    ans = []
    for i in arr:
        ans.append(0)
        for j in range(len(i)):
            if ord(i[j].lower()) - 97 == j:
                ans[-1] += 1
    return ans

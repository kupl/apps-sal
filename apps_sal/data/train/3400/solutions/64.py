def even_numbers(arr, n):
    ans = []
    for i in arr:
        if i % 2 == 0:
            ans.append(i)
    return ans[-n:]

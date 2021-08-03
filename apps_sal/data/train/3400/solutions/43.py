def even_numbers(arr, n):
    ans = []
    for i in arr[::-1]:
        if n == 0:
            break
        if i % 2 == 0:
            ans.append(i)
            n -= 1
    return ans[::-1]

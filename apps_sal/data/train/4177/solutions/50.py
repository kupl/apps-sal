def men_from_boys(arr):
    even = []
    odd = []
    for i in arr:
        if i not in even and i % 2 == 0:
            even.append(i)
        elif i not in odd and i % 2 != 0:
            odd.append(i)
    even.sort()
    odd.sort(reverse=True)
    return even + odd

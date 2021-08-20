def luxhouse(houses):
    lux = 0
    ' \\o/  https://www.youtube.com/watch?v=n0DscZs7SXo  \\o/   ;-D '
    ans = [0] * len(houses)
    for n in range(len(houses) - 1, -1, -1):
        if houses[n] > lux:
            lux = houses[n]
        else:
            ans[n] = lux - houses[n] + 1
    return ans

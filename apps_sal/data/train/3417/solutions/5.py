def cut_the_ropes(arr):
    ans = []
    while arr:
        ans.append(len(arr))
        minRope = min(arr)
        arr = [elt - minRope for elt in arr if elt > minRope]
    return ans

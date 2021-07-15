def int_diff(arr, n):
    count = 0
    position = 0
    for x in arr[position:]:
        for y in arr[position + 1:]:
            diff = (y - x) if (y > x) else (x - y)
            if diff == n:
                count += 1
        position += 1
    return count
